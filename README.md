# RASA-Chatbot

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

The bot takes the following inputs from the user:

City: Take the input from the customer as a text field. For example:

Bot: In which city are you looking for restaurants?

User: anywhere in Delhi

Important Notes: 

Assume that Foodie works only in Tier-1 and Tier-2 cities. You can use the current HRA classification of the cities from here. Under the section 'current classification' on this page, the table categorizes cities as X, Y and Z. Consider 'X ' cities as tier-1 and 'Y' as tier-2. 
The bot should be able to identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc. Chatbot should provide results for tier-1 and tier-2 cities only, while for tier-3 cities, it should reply back with something like "We do not operate in that area yet".


Cuisine Preference: Take the cuisine preference from the customer. The bot should list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that. Following is an example for the same:

Bot: What kind of cuisine would you prefer?

Chinese
Mexican
Italian
American
South Indian
North Indian
User: I’ll prefer Italian!

Average budget for two people: Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. The bot should ask the user to select one of the three price categories. For example:

Bot: What price range are you looking at?

Lesser than Rs. 300
Rs. 300 to 700
More than 700
User: in range of 300 to 700



While showing the results to the user, the bot should display the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.


Finally, the bot should ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot should ask for user’s email id and then send it over email. Else, just reply with a 'goodbye' message. The mail should have the following details for each restaurant:

Restaurant Name
Restaurant locality address
Average budget for two people
Zomato user rating
=======================================================================================

Environment details as given below:

absl-py==0.9.0
aiofiles==0.5.0
aiohttp==3.6.2
alabaster==0.7.12
alembic==1.4.2
APScheduler==3.6.3
argh==0.26.2
astor==0.8.1
astroid @ file:///C:/ci/astroid_1592481955828/work
async-generator==1.10
async-timeout==3.0.1
atomicwrites==1.4.0
attrs==19.3.0
autopep8 @ file:///tmp/build/80754af9/autopep8_1592412889138/work
Babel==2.8.0
backcall==0.2.0
bcrypt==3.1.7
bleach==3.1.5
blis==0.2.4
boto3==1.14.6
botocore==1.17.6
brotlipy==0.7.0
cachetools==4.1.0
certifi==2020.6.20
cffi==1.14.0
chardet==3.0.4
cloudpickle==1.3.0
colorama==0.4.3
colorclass==2.2.0
coloredlogs==10.0
colorhash==1.0.2
cryptography==2.9.2
cycler==0.10.0
cymem==2.0.3
decorator==4.4.2
defusedxml==0.6.0
diff-match-patch==20181111
dnspython==1.16.0
docopt==0.6.2
docutils==0.16
en-core-web-md @ https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.1.0/en_core_web_md-2.1.0.tar.gz
entrypoints==0.3
fbmessenger==6.0.0
flake8==3.8.3
future==0.18.2
gast==0.2.2
gevent==1.5.0
gitdb==4.0.5
GitPython==3.1.3
google-auth==1.18.0
google-auth-oauthlib==0.4.1
google-pasta==0.2.0
greenlet==0.4.16
grpcio==1.29.0
h11==0.8.1
h2==3.2.0
h5py==2.10.0
hpack==3.0.0
hstspreload==2020.6.16
httplib2==0.18.1
httptools==0.1.1
httpx==0.9.3
humanfriendly==8.2
hyperframe==5.2.0
idna==2.9
imagesize==1.2.0
importlib-metadata==1.6.1
intervaltree==3.0.2
ipykernel==5.3.0
ipython @ file:///C:/ci/ipython_1592330400575/work
ipython-genutils==0.2.0
isodate==0.6.0
isort==4.3.21
jedi==0.15.2
Jinja2==2.11.2
jmespath==0.10.0
joblib==0.15.1
jsonpickle==1.4.1
jsonschema==3.2.0
jupyter-client==6.1.3
jupyter-core==4.6.3
kafka-python==1.4.7
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.0
keyring @ file:///C:/ci/keyring_1593109817825/work
kiwisolver==1.2.0
lazy-object-proxy==1.4.3
Mako==1.1.3
Markdown==3.2.2
MarkupSafe==1.1.1
matplotlib==3.2.2
mattermostwrapper==2.2
mccabe==0.6.1
mistune==0.8.4
multidict==4.7.6
murmurhash==1.0.2
nbconvert==5.6.1
nbformat==5.0.7
networkx==2.4
numpy==1.18.5
numpydoc==1.0.0
oauth2client==4.1.3
oauthlib==3.1.0
opt-einsum==3.2.1
packaging==20.4
pandocfilters==1.4.2
paramiko==2.7.1
parso==0.5.2
pathtools==0.1.2
pexpect==4.8.0
pickleshare==0.7.5
pika==1.1.0
plac==0.9.6
pluggy==0.13.1
preshed==2.0.1
prompt-toolkit==2.0.10
protobuf==3.12.2
psutil==5.7.0
psycopg2-binary==2.8.5
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycodestyle==2.6.0
pycparser==2.20
pydocstyle @ file:///tmp/build/80754af9/pydocstyle_1592848020240/work
pydot==1.4.1
pyflakes==2.2.0
Pygments==2.6.1
PyJWT==1.7.1
pykwalify==1.7.0
pylint @ file:///C:/ci/pylint_1592487534522/work
pymongo==3.8.0
PyNaCl @ file:///C:/ci/pynacl_1593121837095/work
pyOpenSSL==19.1.0
pyparsing==2.4.7
pyreadline==2.1
pyrsistent==0.16.0
PySocks==1.7.1
python-crfsuite==0.9.7
python-dateutil==2.8.1
python-editor==1.0.4
python-engineio==3.12.1
python-jsonrpc-server==0.3.4
python-language-server==0.31.9
python-socketio==4.5.1
python-telegram-bot==12.7
pytz==2019.3
pywin32==227
pywin32-ctypes==0.2.0
PyYAML==5.3.1
pyzmq==19.0.1
QDarkStyle==2.8.1
QtAwesome==0.7.2
qtconsole @ file:///tmp/build/80754af9/qtconsole_1592848611704/work
QtPy==1.9.0
questionary==1.5.2
rasa==1.10.3
rasa-sdk==1.10.1
rasa-x==0.29.1
redis==3.5.3
requests @ file:///tmp/build/80754af9/requests_1592841827918/work
requests-oauthlib==1.3.0
requests-toolbelt==0.9.1
rfc3986==1.4.0
rocketchat-API==1.3.1
rope==0.17.0
rsa==4.6
Rtree==0.9.4
ruamel.yaml==0.16.10
ruamel.yaml.clib==0.2.0
s3transfer==0.3.3
sanic==19.12.2
Sanic-Cors==0.10.0.post3
sanic-jwt==1.3.2
Sanic-Plugins-Framework==0.9.2
scikit-learn==0.22.2.post1
scipy==1.4.1
six==1.15.0
sklearn-crfsuite==0.3.6
slackclient==2.7.1
smmap==3.0.4
sniffio==1.1.0
snowballstemmer==2.0.0
sortedcontainers==2.2.2
spacy==2.1.9
Sphinx @ file:///tmp/build/80754af9/sphinx_1592842202926/work
sphinxcontrib-applehelp==1.0.2
sphinxcontrib-devhelp==1.0.2
sphinxcontrib-htmlhelp==1.0.3
sphinxcontrib-jsmath==1.0.1
sphinxcontrib-qthelp==1.0.3
sphinxcontrib-serializinghtml==1.1.4
spyder==4.1.3
spyder-kernels==1.9.1
SQLAlchemy==1.3.17
srsly==1.0.2
tabulate==0.8.7
tensorboard==2.1.1
tensorflow==2.1.1
tensorflow-addons==0.7.1
tensorflow-estimator==2.1.0
tensorflow-hub==0.8.0
tensorflow-probability==0.9.0
termcolor==1.1.0
terminaltables==3.1.0
testpath==0.4.4
thinc==7.0.8
toml @ file:///tmp/build/80754af9/toml_1592853716807/work
tornado==6.0.4
tqdm==4.45.0
traitlets==4.3.3
twilio==6.26.3
typed-ast==1.4.1
tzlocal==2.1
ujson==1.35
urllib3==1.25.9
wasabi==0.6.0
watchdog==0.10.2
wcwidth==0.2.4
webencodings==0.5.1
webexteamssdk==1.3
websockets==8.1
Werkzeug==1.0.1
win-inet-pton==1.1.0
wincertstore==0.2
wrapt==1.12.1
yapf @ file:///tmp/build/80754af9/yapf_1592847929485/work
yarl==1.4.2
zipp==3.1.0

