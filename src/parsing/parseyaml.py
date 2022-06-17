# Fill in this file with the code from parsing YAML exercise

import json
import yaml

yaml_file = open("myfile.yaml","r")

pythondata = yaml.safe_load(yaml_file)

print(pythondata['expires_in'])

print("The access token from YAML is: %s" % pythondata['access_token'])

print("\n\n")

print(json.dumps(pythondata))

"""
EXPECTED OUTPUT:
________________
developer:src > cd parsing/
developer:parsing > python parseyaml.py 
1209600
The access token from YAML is: ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3



{"access_token": "ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3", "expires_in": 1209600, "refresh_token": "MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4", "refreshtokenexpires_in": 7776000}
"""
