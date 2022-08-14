from urllib import response
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

#Load env tokens
load_dotenv()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_API_TOKEN']
oktaToken = os.environ['OKTA_TOKEN']

#define okta header
oktaPayload = ""
oktaHeaders = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': "SSWS" + oktaToken
    }

#okta function - List Users
def oktaListUsers():
    print("Pulling data...")
    #Get requests from OKTA
    url = "https://dev-9849447.okta.com/api/v1/users/me"
    response = requests.request("GET", url, data=oktaPayload, headers=oktaHeaders)
    status = response.status_code
    data = response.json()
    
    for prop in data:
        email = str(prop['profile']['email'])
        firstName = str(prop['profile']['firstName'])
        lastName = str(prop['profile']['lastName'])
        userInfo = firstName +' ' + lastName + ' : ' + email
        print(userInfo)
    
    print(status)
    

#Okta Function - Create user
def oktaCreateUser(userFirst, userLast, userEmail, mobilePhone, passwordGen):
    
    params = {
        'activate': 'true',}
    json_data = {
        'profile': {
        'firstName': userFirst,
        'lastName': userLast,
        'email': userEmail,
        'login': userEmail,
        'mobilePhone': mobilePhone,
        }
    }
    #Url Call
    response = requests.post('"https://dev-9849447.okta.com/api/v1/users', params=params, headers=oktaHeaders, json=json_data)
    status = response.status_code
    print(status)

#okta function - specific user attributes passed to function from slack app need to pass email
def oktaGetUserAttr(email):
    print("Finding user attribute...")
    url = "https://dev-9849447.okta.com/api/v1/users/"+ email
    response = requests.request("GET", url, data=oktaPayload, headers=oktaHeaders)
    status = response.status_code
    data = response.json()
    # print(data)
    email = str(data['profile']['email'])
    userId = str(data['type']['id'])
    # not needed?
    # firstName = str(data['profile']['firstName'])
    # lastName = str(data['profile']['lastName'])
    userStatus = str(data['status'])
    userInfo = 'Email: ' + email +'\nID: ' + userId + '\nStatus: ' + userStatus
    print(status)
    return(userInfo)
    

#slack code
app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
def mention_handler(body, say):
        say("Hi I'm Chatty, I can help you add, remove and just get information on users in this workspace!! :)\n what would you like to do? Type 'next' to get started:")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_API_TOKEN"]).start()
