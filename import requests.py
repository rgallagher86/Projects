import csv
import requests
import os

path = os.getcwd()
print(path) 
url = 'https://gorest.co.in/public/v2/users'  

headers = { "content-type": "application/json" }

response = requests.get(url,headers)

print(response.status_code)

data = response.json()
#data = data['Data']

csvHeader = 'id,email' 
with open(str(path) + "\\emaillist.csv","w") as f:
    writer = csv.writer(f)
    print(csvHeader)
    for value in data:
        email = str(value['email'])
        userId = str(value['id'])
        status = str(value['status'])
        row = userId + ',' + email
        if email.endswith('.io') and status == 'active':
            print(row)
            print(status)
            f.write(row)