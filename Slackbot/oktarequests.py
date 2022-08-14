from distutils.log import error
import requests
import os
from dotenv import load_dotenv

load_dotenv()
oktaToken = os.environ['OKTA_TOKEN']
print(oktaToken)

payload = ""
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': "SSWS" + oktaToken
    }

print("Type GET to pull data \nType CREATE to create user \nType DELETE to delete user")
userChoice = input("")
if 'get' in userChoice.lower():
    print("Pulling data...")
    #Get requests from OKTA
    url = "https://dev-9849447.okta.com/api/v1/users"
    response = requests.request("GET", url, data=payload, headers=headers)
    status = response.status_code
    data = response.json()
    for prop in data:
        email = str(prop['profile']['email'])
        userId = str(prop['id'])
        firstName = str(prop['profile']['firstName'])
        lastName = str(prop['profile']['lastName'])
        userName = firstName +' ' + lastName
        userInfo = firstName +' ' + lastName + ' : ' + email
        print(userInfo)
    
        
elif 'create' in userChoice.lower():
    print("Updating data...")
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

    response = requests.post('"https://dev-9849447.okta.com/api/v1/users', params=params, headers=headers, json=json_data)
    status = response.status_code

elif 'delete' in userChoice.lower():
    print("Deleting data...")
    #Get requests from OKTA
    email = 'ryan@codeclimate.com'
    url = "https://dev-9849447.okta.com/api/v1/users/"+ email
    response = requests.request("GET", url, data=payload, headers=headers)
    status = response.status_code
    data = response.json()
    # print(data)
    # dataLen = data.length()
    # print(dataLen)
    # for prop in data:
    #     print(prop)
    #     print(prop['profile'])
    print(data)
    email = str(data['profile']['email'])
    userId = str(data['type']['id'])
    firstName = str(data['profile']['firstName'])
    lastName = str(data['profile']['lastName'])
    userStatus = str(data['status'])
    userInfo = 'Email: ' + email +'\nID: ' + userId + '\nStatus: ' + userStatus
    print(userInfo)
    # return(userInfo)
    

else:
    print("Error in response")
    error    
    
# if status == '200':
#     print(response.text)
# else:
#     print("Error with connection: Code - " + response.status_code)