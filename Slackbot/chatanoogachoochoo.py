from urllib import response
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

#Load env tokens
load_dotenv()
SLACK_BOT_TOKEN = os.environ['API_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['API_SLACK_TOKEN']
oktaToken = os.environ['OKTA_TOKEN']

print(SLACK_APP_TOKEN)
print(SLACK_BOT_TOKEN)
print(oktaToken)

oktaPayload = ""
oktaHeaders = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': "SSWS" + oktaToken
    }

#okta function - Get request
def oktaGet():
    print("Pulling data...")
    #Get requests from OKTA
    url = "https://dev-9849447.okta.com/api/v1/users/me"
    response = requests.request("GET", url, data=oktaPayload, headers=oktaHeaders)
    status = response.status_code
    
def oktaCreate():
    #define user data
    userFirst = ''
    userLast = ''
    userEmail = ''
    mobilePhone = ''
    passwordGen = ''
    params = {
        'activate': 'true',}
    json_data = {
        'profile': {
        'firstName': userFirst,
        'lastName': userLast,
        'email': userEmail,
        'login': userEmail,
        'mobilePhone': mobilePhone,
        },
        'credentials': {
            'password': {
                'value': passwordGen,
                        },
                    },
                }
    response = requests.post('"https://dev-9849447.okta.com/api/v1/users', params=params, headers=oktaHeaders, json=json_data)
    status = response.status_code


def oktaRemove():
    print("Deleting data...")

#slack code
app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
def mention_handler(body, say):
        say("Hi I'm Chatty, I can help you add, remove and just get information on users in this workspace!! :)\n what would you like to do? Type 'next' to get started:")
        
# if (payload.event.text.includes("tell me a joke")) {
   
            
            




if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()



# Start the app
# if __name__ == "__main__":
#         handler = SocketModeHandler(app, SLACK_APP_TOKEN)
#         handler.start()
