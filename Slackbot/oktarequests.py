import requests
import os
from dotenv import load_dotenv

url = "https://dev-9849447.okta.com/api/v1/users/me"

load_dotenv()
oktaToken = os.environ['OKTA_TOKEN']
print(oktaToken)

payload = ""
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': "SSWS" + oktaToken
    }

response = requests.request("GET", url, data=payload, headers=headers)
print(response.status_code)
print(response.text)