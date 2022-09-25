## Path with no deatils1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"place": "delhi"}
    - slot{"place": "delhi"}
	- action_verify_location
    - slot{"place": "delhi"}
    - slot{"place_valid":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"minprice":"300", "maxprice":"700"}
    - slot{"minprice": "300"}
    - slot{"maxprice": "700"}
	- action_verify_budget
    - slot{"minprice": "300"}
    - slot{"maxprice": "700"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "delhi"}
    - utter_ask_email
* affirm
	- utter_ask_emailid
* send_mail{"emailid": "sreenathsnair@gmail.com"}
    - slot{"emailid": "sreenathsnair@gmail.com"}
	- action_send_email
	- utter_goodbye
	- action_restart

## Path with place2
* greet
    - utter_greet
* restaurant_search{"place": "bangalore"}
    - slot{"place": "bangalore"}
	- action_verify_location
    - slot{"place": "bangalore"}
    - slot{"place_valid":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
	- action_verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"maxprice":"300"}
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
	- action_verify_budget
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "bangalore"}
    - utter_ask_email
* affirm
	- utter_ask_emailid
* send_mail{"emailid": "abc2900@yahoo.com"}
    - slot{"emailid": "abc2900@yahoo.com"}
	- action_send_email
	- utter_goodbye
	- action_restart

## Path with cuisine3
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
	- action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_valid":true}
    - utter_ask_location
* restaurant_search{"place": "kolkata"}
    - slot{"place": "kolkata"}
	- action_verify_location
    - slot{"place": "kolkata"}
    - slot{"place_valid":true}	
    - utter_ask_budget
* restaurant_search{"minprice":"300", "maxprice":"500"}
    - slot{"minprice": "300"}
    - slot{"maxprice": "500"}
	- action_verify_budget
    - slot{"minprice": "0"}
    - slot{"maxprice": "5000"}
    - slot{"budget_valid":false}
    - utter_ask_budget
* restaurant_search{"minprice":"300", "maxprice":"700"}
    - slot{"minprice": "300"}
    - slot{"maxprice": "700"}
	- action_verify_budget
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "kolkata"}
    - utter_ask_email
* affirm
	- utter_ask_emailid
* send_mail{"emailid": "chirag123@gmail.co.in"}
    - slot{"emailid": "chirag123@gmail.co.in"}
	- action_send_email
	- utter_goodbye
	- action_restart

## Path with cuisine and place4
* greet
    - utter_greet
* restaurant_search{"place": "chennai", "cuisine": "italian"}
    - slot{"place": "chennai"}
    - slot{"cuisine": "italian"}
	- action_verify_location
    - slot{"place": "chennai"}
    - slot{"place_valid":true}	
	- action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"minprice":"700"}
    - slot{"minprice": "700"}
    - slot{"maxprice": "5000"}
	- action_verify_budget
    - slot{"minprice": "700"}
    - slot{"maxprice": "5000"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "chennai"}
    - utter_ask_email
* deny
	- utter_goodbye
	- action_restart

## Path with place not existing5
* greet
    - utter_greet
* restaurant_search{"place": "alleppey"}
    - slot{"place": "alleppey"}
	- action_verify_location
    - slot{"place":null}
    - slot{"place_valid":false}
    - utter_ask_location
* restaurant_search{"place": "mumbai"}
    - slot{"place": "mumbai"}
	- action_verify_location
    - slot{"place": "mumbai"}
    - slot{"place_valid":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
	- action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"minprice":"700"}
    - slot{"minprice": "700"}
    - slot{"maxprice": "5000"}
	- action_verify_budget
    - slot{"minprice": "700"}
    - slot{"maxprice": "5000"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "mumbai"}
    - utter_ask_email
* affirm
	- utter_ask_emailid
* send_mail{"emailid": "john345@rediff.co.uk"}
    - slot{"emailid": "john345@rediff.co.uk"}
	- action_send_email
	- utter_goodbye
	- action_restart

## Path with place but invalid cuisine6
* greet
    - utter_greet
* restaurant_search{"place": "hyderabad"}
    - slot{"place": "hyderabad"}
	- action_verify_location
    - slot{"place": "hyderabad"}
    - slot{"place_valid":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "continental"}
    - slot{"cuisine": "continental"}
	- action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_valid":false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
	- action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"maxprice":"300", "maxprice":"700"}
    - slot{"minprice": "300"}
    - slot{"maxprice": "700"}
	- action_verify_budget
    - slot{"minprice": "300"}
    - slot{"maxprice": "700"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "hyderabad"}
    - utter_ask_email
* deny
	- utter_goodbye
	- action_restart

## Path with no deatils7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"place": "rishikesh"}
    - slot{"place": "rishikesh"}
	- action_verify_location
    - slot{"place": null}
    - slot{"place_valid":false}	
    - utter_ask_location
* restaurant_search{"place": "ahmedabad"}
    - slot{"place": "ahmedabad"}
	- action_verify_location
    - slot{"place": "ahmedabad"}
    - slot{"place_valid":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"minprice":"700"}
    - slot{"minprice": "700"}
    - slot{"maxprice": "5000"}
	- action_verify_budget
    - slot{"minprice": "700"}
    - slot{"maxprice": "5000"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "ahmedabad"}
    - utter_ask_email
* affirm
	- utter_ask_emailid
* send_mail{"emailid": "eeshu2017@ymail.com"}
    - slot{"emailid": "eeshu2017@ymail.com"}
	- action_send_email
	- utter_goodbye
	- action_restart
	
## Path with cuisine and place8
* greet
    - utter_greet
* restaurant_search{"place": "nagpur",  "cuisine": "mexican"}
    - slot{"place": "nagpur"}
    - slot{"cuisine": "mexican"}
	- action_verify_location
    - slot{"place": "nagpur"}
    - slot{"place_valid":true}	
	- action_verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"maxprice":"300"}
    - slot{"minprice": "0"}
    - slot{"minprice": "300"}
	- action_verify_budget
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "nagpur"}
    - utter_ask_email
* affirm
	- utter_ask_emailid
* send_mail{"emailid": "krish1988@gmail.com"}
    - slot{"emailid": "krish1988@gmail.com"}
	- action_send_email
	- utter_goodbye
	- action_restart
	
## Path with cuisine and place9
* greet
    - utter_greet
* restaurant_search{"place": "coimbatore",  "cuisine": "american"}
    - slot{"place": "coimbatore"}
    - slot{"cuisine": "american"}
	- action_verify_location
    - slot{"place": "coimbatore"}
    - slot{"place_valid":true}	
	- action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"maxprice":"400"}
    - slot{"minprice": "0"}
    - slot{"maxprice": "400"}
	- action_verify_budget
    - slot{"minprice": "0"}
    - slot{"maxprice": "5000"}
    - slot{"budget_valid": false}
    - utter_ask_budget
* restaurant_search{"maxprice":"300"}
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
	- action_verify_budget
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "coimbatore"}
    - utter_ask_email
* deny
	- utter_goodbye
	- action_restart


## Path with place not existing10
* greet
    - utter_greet
* restaurant_search{"place": "panaji"}
    - slot{"place": "panaji"}
	- action_verify_location
    - slot{"place":null}
    - slot{"place_valid":false}
    - utter_ask_location
* restaurant_search{"place": "hasan"}
    - slot{"place": "hasan"}
	- action_verify_location
    - slot{"place":null}
    - slot{"place_valid":false}	
    - utter_ask_location
* restaurant_search{"place": "guwahati"}
    - slot{"place": "guwahati"}
	- action_verify_location
    - slot{"place": "guwahati"}
    - slot{"place_valid":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
	- action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"minprice":"300", "maxprice":"700"}
    - slot{"minprice": "300"}
    - slot{"maxprice": "700"}
	- action_verify_budget
    - slot{"minprice": "300"}
    - slot{"maxprice": "700"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "guwahati"}
    - utter_ask_email
* affirm
	- utter_ask_emailid
* send_mail{"emailid": "krishna345676@yahoo.co.in"}
    - slot{"emailid": "krishna345676@yahoo.co.in"}
	- action_send_email
	- utter_goodbye
	- action_restart


## Path with cuisine not existing11
* greet
    - utter_greet
* restaurant_search{"place": "nagpur"}
    - slot{"place": "nagpur"}
	- action_verify_location
    - slot{"place":"nagpur"}
    - slot{"place_valid":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
	- action_verify_cuisine
    - slot{"cuisine":null}
    - slot{"cuisine_valid":false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
	- action_verify_cuisine
    - slot{"cuisine":null}
    - slot{"cuisine_valid":false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_verify_cuisine
    - slot{"cuisine":"chinese"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"minprice":"150", "maxprice":"400"}
    - slot{"minprice": "150"}
    - slot{"maxprice": "400"}
	- action_verify_budget
    - slot{"minprice": "0"}
    - slot{"maxprice": "5000"}
    - slot{"budget_valid": false}
    - utter_ask_budget
* restaurant_search{"maxprice":"300"}
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
	- action_verify_budget
    - slot{"minprice":"0"}
    - slot{"maxprice":"300"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "nagpur"}
    - utter_ask_email
* deny
	- utter_goodbye
	- action_restart

## Path with no deatils invalid place12
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"place": "amarnath"}
    - slot{"place": "amarnath"}
	- action_verify_location
    - slot{"place": null}
    - slot{"place_valid":false}	
    - utter_ask_location
* restaurant_search{"place": "Kochi"}
    - slot{"place": "Kochi"}
	- action_verify_location
    - slot{"place": "kochi"}
    - slot{"place_valid":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
	- action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_valid":false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"minprice":"700"}
    - slot{"minprice": "700"}
	- action_verify_budget
    - slot{"minprice": "700"}
    - slot{"maxprice": "5000"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "kochi"}
    - utter_ask_email
* affirm
	- utter_ask_emailid
* send_mail{"emailid": "eeshu2017@ymail.com"}
    - slot{"emailid": "eeshu2017@ymail.com"}
	- action_send_email
	- utter_goodbye
	- action_restart

## interactive_story_13
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"place": "bangalore"}
    - slot{"place": "bangalore"}
    - action_verify_location
    - slot{"place": "bangalore"}
    - slot{"place_valid": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_valid": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"minprice": "300", "maxprice": "700"}
    - slot{"maxprice": "700"}
    - slot{"minprice": "300"}
    - action_verify_budget
    - slot{"minprice": 300.0}
    - slot{"maxprice": 700.0}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "bangalore"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_14
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"place": "kochi"}
    - slot{"place": "kochi"}
    - action_verify_location
    - slot{"place": "kochi"}
    - slot{"place_valid": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Srilankan"}
    - slot{"cuisine": "Srilankan"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_valid": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"minprice": "300", "maxprice": "700"}
    - slot{"maxprice": "700"}
    - slot{"minprice": "300"}
    - action_verify_budget
    - slot{"minprice": 300.0}
    - slot{"maxprice": 700.0}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "kochi"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "nainu123@abc.com"}
    - slot{"emailid": "nainu123@abc.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"cuisine": "Arabian"}
    - slot{"cuisine": "Arabian"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_valid": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mediterranian"}
    - slot{"cuisine": "Mediterranian"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_valid": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_valid": true}
    - utter_ask_location
* restaurant_search{"place": "srinagar"}
    - slot{"place": "srinagar"}
    - action_verify_location
    - slot{"place": "srinagar"}
    - slot{"place_valid": true}
    - utter_ask_budget
* restaurant_search{"maxprice": "300"}
    - slot{"maxprice": "300"}
    - slot{"minprice": "0"}
    - action_verify_budget
    - slot{"minprice": 0.0}
    - slot{"maxprice": 300.0}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "srinagar"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"cuisine": "Carribean"}
    - slot{"cuisine": "Carribean"}
	- action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_valid":false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_valid": true}
    - utter_ask_location
* restaurant_search{"place": "kolkata"}
    - slot{"place": "kolkata"}
	- action_verify_location
    - slot{"place": "kolkata"}
    - slot{"place_valid":true}	
    - utter_ask_budget
* restaurant_search{"minprice":"700"}
    - slot{"maxprice": "5000"}
    - slot{"maxprice": "700"}
	- action_verify_budget
    - slot{"minprice": "700"}
    - slot{"maxprice": "5000"}
    - slot{"budget_valid":true}
    - action_search_restaurants
    - slot{"place": "kolkata"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"place": "ahmedabad",  "cuisine": "japanese"}
    - slot{"place": "ahmedabad"}
    - slot{"cuisine": "japanese"}
	- action_verify_location
    - slot{"place": "ahmedabad"}
    - slot{"place_valid":true}	
	- action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_valid":false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"maxprice":"300"}
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
	- action_verify_budget
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "ahmedabad"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "pinky_cat@abc.com"}
    - slot{"emailid": "pinky_cat@abc.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"place": "thane",  "cuisine": "american"}
    - slot{"place": "thane"}
    - slot{"cuisine": "american"}
	- action_verify_location
    - slot{"place": null}
    - slot{"place_valid":false}	
	- action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_valid":true}
    - utter_ask_location
* restaurant_search{"place": "kolkata"}
    - slot{"place": "kolkata"}
	- action_verify_location
    - slot{"place": "kolkata"}
    - slot{"place_valid":true}	
    - utter_ask_budget
* restaurant_search{"maxprice":"300"}
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
	- action_verify_budget
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "kolkata"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "sulu346@abc.com"}
    - slot{"emailid": "sulu346@abc.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## Path with place not existing and wrong cuisine19
* greet
    - utter_greet
* restaurant_search{"place": "Kedarnath"}
    - slot{"place": "Kedarnath"}
	- action_verify_location
    - slot{"place":null}
    - slot{"place_valid":false}
    - utter_ask_location
* restaurant_search{"place": "salem"}
    - slot{"place": "salem"}
	- action_verify_location
    - slot{"place": "salem"}
    - slot{"place_valid":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "german"}
    - slot{"cuisine": "german"}
	- action_verify_cuisine
    - slot{"cuisine":null}
    - slot{"cuisine_valid":false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_verify_cuisine
    - slot{"cuisine":"chinese"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"maxprice":"300"}
    - slot{"minprice": "0"}
    - slot{"minprice": "300"}
	- action_verify_budget
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "salem"}
    - utter_ask_email
* affirm
	- utter_ask_emailid
* send_mail{"emailid": "chirag.shashi@ora.com"}
    - slot{"emailid": "chirag.shashi@ora.com"}
	- action_send_email
	- utter_goodbye
	- action_restart

## Path with cuisine and place_20
* greet
    - utter_greet
* restaurant_search{"place": "visakhapatnam", "cuisine": "mexican"}
    - slot{"place": "visakhapatnam"}
    - slot{"cuisine": "mexican"}
	- action_verify_location
    - slot{"place": "visakhapatnam"}
    - slot{"place_valid":true}
	- action_verify_cuisine
    - slot{"cuisine":"mexican"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"minprice": "300", "maxprice":"700"}
    - slot{"minprice": "300"}
    - slot{"minprice": "700"}
	- action_verify_budget
    - slot{"minprice": "300"}
    - slot{"maxprice": "700"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "visakhapatnam"}
    - utter_ask_email
* deny
	- utter_goodbye
	- action_restart

## Path with no deatils21
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"place": "mysore"}
    - slot{"place": "mysore"}
	- action_verify_location
    - slot{"place": "mysore"}
    - slot{"place_valid":true}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
	- action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_valid":true}
    - utter_ask_budget
* restaurant_search{"maxprice":"300"}
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
	- action_verify_budget
    - slot{"minprice": "0"}
    - slot{"maxprice": "300"}
    - slot{"budget_valid": true}
    - action_search_restaurants
    - slot{"place": "mysore"}
    - utter_ask_email
* affirm
	- utter_ask_emailid
* send_mail{"emailid": "abc1234@gmail.com"}
    - slot{"emailid": "abc1234@gmail.com"}
	- action_send_email
	- utter_goodbye
	- action_restart