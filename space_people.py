#! /usr/bin/env python3

''' List the current people in space.
    HTTP request to api.open-notify.org/astros.json
    JSON is data format which is a mix of lists and dictionaries.

    format of JSON returned:

    {
        "message": "success",
        "number": NUMBER_OF_PEOPLE_IN_SPACE,
        "people": [
            {"craft": SPACECRAFT_NAME, "name": NAME},
            ...
         ]
     }    
'''

import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print("The people currently in space are:")
for person in json['people']:
    print(f"{person['name']:<25} {person['craft']:<20}")

