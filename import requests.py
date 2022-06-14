import requests
city = 'toronto'
api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'Mjvc+QDmZJZ0KEJCYu2L/Q==qxTZL4b8DNJ9zrTI'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)