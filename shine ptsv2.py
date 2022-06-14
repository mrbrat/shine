from email import header
import requests, random

api_url = 'https://ptsv2.com/t/brat/post'
usernumber = random.randint(0,150)
payload =  { "userId" : usernumber,
"username": 'shine',
"userpass" : 'brat'}

headers = {'content-type': 'application/json'}

r = requests.post (api_url, auth=('shine', 'brat'),data=payload, headers=headers)

get_url = 'https://ptsv2.com/t/brat#'
g = requests.get(get_url)
print((g.json))
