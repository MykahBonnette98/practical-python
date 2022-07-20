#API requests

import requests

repsonse = requests.get('http://api.open-notify.org/astros.json')
json = repsonse.json()

#not using loop 
print(json)

#using a for loop to only get people
for person in json['people']:
    print(person)

for person in json['people']:
    print(person['name']) 

#console result using for loop for peoples names
# Oleg Artemyev
# Denis Matveev
# Sergey Korsakov
# Kjell Lindgren
# Bob Hines

#console result using loop for people
# {'name': 'Oleg Artemyev', 'craft': 'ISS'}
# {'name': 'Denis Matveev', 'craft': 'ISS'}
# {'name': 'Sergey Korsakov', 'craft': 'ISS'}
# {'name': 'Kjell Lindgren', 'craft': 'ISS'}

#consule result before using the loop 
# {'number': 10, 'people': [{'name': 'Oleg Artemyev', 'craft': 'ISS'}, 
# {'name': 'Denis Matveev', 'craft': 'ISS'}, 
# {'name': 'Chen Dong', 'craft': 'Tiangong'}, 
# {'name': 'Liu Yang', 'craft': 'Tiangong'}], 'message': 'success'}