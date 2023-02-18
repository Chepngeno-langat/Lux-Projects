import requests
from bs4 import BeautifulSoup

response = requests.get('https://randomuser.me/api/?results=100')
#print(response.status_code)

data = response.json()["results"]
# first_name = data[0]["name"]["first"]
# last_name = data[0]["name"]["last"]
# print(first_name + ' ' + last_name)

i = 0
names = []
while (i < 100):
    first_name = data[i]["name"]["first"]
    last_name = data[i]["name"]["last"]
    #print(first_name + ' ' + last_name)
    full_name = first_name + ' ' + last_name
    names.append(full_name)
    i += 1
print(names)

# randomuser_webpage = response.text
# print(randomuser_webpage)
# soup = BeautifulSoup(randomuser_webpage, 'html.parser')
#
# first_name = soup.find_all('first')
# print(first_name)
