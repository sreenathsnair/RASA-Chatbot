# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from email.message import EmailMessage
import smtplib
import zomatopy
import json
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

search_results = []
class ActionSearchRestaurant(Action):
    
    def name(self) -> Text:
        return "action_search_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global search_results;
        search_results = []
        place = tracker.get_slot('place')
        cuisine = tracker.get_slot('cuisine')
        minprice = tracker.get_slot('minprice')
        maxprice = tracker.get_slot('maxprice')
        if(minprice):
            try:
                minprice = float(minprice)
            except:
                minprice = 0
        else:
            minprice = 0
        if(maxprice):
            try:
                maxprice = float(maxprice)
            except:
                maxprice = 0
        else:
            maxprice = 0

        print("After check Min Max Price: ", (minprice, maxprice))
        if(maxprice < minprice):
            temp = minprice;
            minprice = maxprice
            maxprice = temp
        msg = "place: "+place+", cuisine: "+cuisine+", minprice: "+str(minprice)+", maxprice: "+str(maxprice);
        print(msg)
        #config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
        config={ "user_key":"9730734629992af9dabd89edd7d78385"}
        zomato = zomatopy.initialize_app(config)
        location_detail=zomato.get_location(place, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'north indian':50,'south indian':85}
        executor = ThreadPoolExecutor(max_workers=5)
        futuresArray  = []
        for start in [0, 20, 40, 60, 80]:
            fut = executor.submit(zomato.restaurant_search, "", lat, lon, str(cuisines_dict.get(cuisine)), start, 20)
            futuresArray.append(fut)
        concurrent.futures.wait(futuresArray, 7)
        result_set = []
        for fut in futuresArray:
            d = json.loads(fut.result())
            result_set = result_set + d['restaurants']

        filtered_res = []
        filtered_res = list(filter(lambda res: float(res['restaurant']['average_cost_for_two']) <= maxprice and  int(res['restaurant']['average_cost_for_two']) >= minprice, result_set))
        filtered_res = [{'name': x['restaurant']['name'], 
                         'address': x['restaurant']['location']['address'], 
                         'rating': float(x['restaurant']['user_rating']['aggregate_rating']), 
                         'average_cost_for_two':float(x['restaurant']['average_cost_for_two'])} for x in filtered_res]

        search_results = filtered_res[:10]
        response=""
        i = 0
        if len(search_results) == 0:
            response= "no results"
        else:
            for restaurant in search_results:
                response = response+ restaurant['name']+ " in "+ restaurant['address']+ " has been rated " + str(restaurant['rating'])+"\n"
                i = i+1
                if i >= 5:
                    break
        print(response)
        dispatcher.utter_message(response)
        return [SlotSet('place', place)]

class ActionVerifyLocation(Action):

    def __init__(self):
        self.city = ['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 
                     'mumbai', 'pune', 'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 
                     'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 
                     'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city', 'chandigarh',
                     'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 
                     'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 
                     'gurgaon', 'guwahati', 'hamirpur', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur',
                     'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 
                     'kannur', 'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana',
                     'lucknow','madurai','malappuram', 'mathura', 'goa',  'mangalore', 'meerut', 'moradabad', 
                     'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'patna', 'pondicherry', 
                     'purulia', 'prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 
                     'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'surat', 'thiruvananthapuram', 
                     'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 
                     'vasai-virar city', 'vijayawada', 'visakhapatnam', 'vellore', 'warangal']

    def name(self) -> Text:
        return "action_verify_location"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = tracker.get_slot('place')
        #Debug only
        print("Place:", place)
        if place and (place.lower() in self.city):
            print("Location valid")
            return [SlotSet('place', place), SlotSet("place_valid", True)]
        else:
            print("Location invalid")
            message = "We do not operate in "+ place+" yet. You may please try another city"
            dispatcher.utter_message(text = message)
            return [SlotSet('place', None), SlotSet("place_valid", False)]

class ActionVerifyCuisine(Action):

    def __init__(self):
        self.supported_cusine = ['chinese', 'mexican', 'italian', 'american', 'south indian', 'north indian']

    def name(self) -> Text:
        return "action_verify_cuisine"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        cuisine = tracker.get_slot('cuisine')
        #Debug only
        print("Cuisine:", cuisine)
        if cuisine and (cuisine.lower() in self.supported_cusine):
            print("Cuisine valid")
            return [SlotSet('cuisine', cuisine), SlotSet("cuisine_valid", True)]
        else:
            print("Cuisine invalid")
            message = "Sorry we dont support "+ cuisine+" cuisine. You may please try another cuisine"
            dispatcher.utter_message(text = message)
            return [SlotSet('cuisine', None), SlotSet("cuisine_valid", False)]

class ActionVerifyBudget(Action):

    def name(self) -> Text:
        return "action_verify_budget"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        minprice = tracker.get_slot("minprice")
        maxprice = tracker.get_slot("maxprice")
        print("Min Max Price: ", (minprice, maxprice))
        if(minprice):
            try:
                minprice = float(minprice)
            except:
                minprice = 0
        else:
            minprice = 0
        if(maxprice):
            try:
                maxprice = float(maxprice)
            except:
                maxprice = 0
        else:
            maxprice = 0
        print("After check Min Max Price: ", (minprice, maxprice))
        if(maxprice < minprice):
            temp = minprice;
            minprice = maxprice
            maxprice = temp

        if ((minprice == 0 and maxprice == 300) or
            (minprice == 300 and maxprice == 700) or
            (minprice == 700 and maxprice == 5000)):
            print("budget valid")
            return [SlotSet('minprice', minprice), 
                    SlotSet("maxprice", maxprice),
                    SlotSet("budget_valid", True)]
        else:
            print("Budget invalid")
            message = "Sorry the price range not supported"
            dispatcher.utter_message(text = message)
            return [SlotSet('minprice', 0), 
                    SlotSet("maxprice", 5000),
                    SlotSet("budget_valid", False)]

class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        emailid = tracker.get_slot('emailid')
        if emailid:
            try:
                print("Email id is valid:", emailid)
                self.send_email(emailid)
                message = "Email Sent! Have a good time"
                dispatcher.utter_message(message);
                return [SlotSet('emailid', emailid)]
            except:
                message = "Something Went Wrong :-( Unable to send the email"
                print(message)
                dispatcher.utter_message(message);
                return [SlotSet('emailid', None)]
        else:
            message = "Email Id is incorrect..."
            dispatcher.utter_message(text = message)
            return [SlotSet('emailid', None)]

    def send_email(self, emailid):
        #If 25 not working try 587. Make sure the ports are not blocked by Firewall
        global search_results
        if(len(search_results) > 0):
            email_body = "Plese find the list of top 10 restaurants as per your search: \n"
        else:
            email_body = "Sorry we could not find any restaurants with your search criteria \n"
        server = smtplib.SMTP("smtp.gmail.com", 25)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("restrochatbot@gmail.com", "Eeshu@2626")
        for restaurant in search_results:
            email_body = email_body+ restaurant['name']+ " in "+ restaurant['address']+ " has been rated " + str(restaurant['rating'])+ " and average cost for two is "+str(restaurant['average_cost_for_two'])+"\n"
        email_body = email_body + ("Have a great time! Visit again. \n")
        #Create Message and populate the fields 
        msg = EmailMessage()
        msg['Subject'] = "Top 10 Restaurants"
        msg['From'] = "restrochatbot@gmail.com"
        msg['To'] = emailid
        msg.set_content(email_body)

        #send the message
        server.send_message(msg)
        server.quit()
        