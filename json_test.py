import json

from urllib.request import urlopen

# with open('states.json') as f:
#     data = json.load(f)

# for state in data['states']:
#     del state['area_codes']

# with open('new_states.json','w') as fw:
#     json.dump(data,fw,indent=2,sort_keys=True)

end_point = 'https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json'

with urlopen(end_point) as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data,indent=2))

print(len(data['list']['resources']))
