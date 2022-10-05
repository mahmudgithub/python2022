#jsondta encode and decode
import json
data={
    'name': 'mahmud',
    'age': 55,
    'coun':'bangladesh'}
json_n = json.dumps(data)
print(json_n)

#OR

import json
data={
    'name': 'mahmud',
    'age': 55,
    'coun':'bangladesh'}
json_encoded_str = json.dumps(data)
print(json_encoded_str)

json_decode= json.loads(json_encoded_str)
print(json_decode)

# write a json data

data = {
    'name': 'mahmud',
    'age': 55,
    'country':'bangladesh'
    }

import json

with open('data/json_data.json','w') as fobj:
    json.dump(data,fobj)

# read a json data
with open('data/json_data.json','r') as fobj:
    json_data=json.load(fobj)
    print(json_data)

