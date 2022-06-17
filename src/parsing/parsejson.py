# Fill in this file with the code from parsing JSON exercise

import json
import yaml

with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)

json_file.close()
print(ourjson)

print(ourjson['expires_in'])

print("The access token from JSON is: %s" % ourjson['access_token'])

print("\n\n---")

#Prints the YAML for this
print(yaml.dump(ourjson))


"""
EXPECTED OUTPUT:
----------------
{'access_token': 'ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3', 'expire
s_in': 1209600, 'refresh_token': 'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMz
Q1Njc4', 'refreshtokenexpires_in': 7776000}
1209600
The access token from JSON is: ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItY
TU3


---
access_token: ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3
expires_in: 1209600
refresh_token: MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4
refreshtokenexpires_in: 7776000
"""
