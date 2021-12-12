# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://prototypingsite.atlassian.net/rest/api/3/search"

auth = HTTPBasicAuth("abdiwali96@gmail.com","R75qpeg4u2qYP0MDxLKE0470")

headers = {
   "Accept": "application/json"
}

query = {
   'jql': 'project = DEP'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


