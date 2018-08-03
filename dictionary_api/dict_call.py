import requests
import json
import pprint
import Config
pp = pprint.PrettyPrinter(indent=2)
# from flask import jsonify

app_id = Config.ox_dict_app_id
app_key = Config.ox_dict_app_key

language = 'en'
word_id = 'Ace'

def get_dictionary_response(word):
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower()
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    # print("json \n" + json.dumps(r.json()))
    # print(r.json())
    return r.json()

car_response = get_dictionary_response("car")
print(car_response)

print("********************************")
print("this is the car_response")
pp.pprint(car_response)
print("********************************")
print("this is the metadata value")
pp.pprint(car_response['metadata'])
print("********************************")
print("this is the results value")
pp.pprint(car_response['results'])
print("********************************")
print("this is the first result")
pp.pprint(car_response['results'][0])

print("********************************")
print("this is the first result lexicalEntries")
pp.pprint(car_response['results'][0]['lexicalEntries'])