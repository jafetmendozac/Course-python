import json
import requests
import sys

if len(sys.argv) != 2:
  sys.exit()


# response = requests.get("https://jsonplaceholder.typicode.com/" + sys.argv[1]) #posts  comments
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) #weezer

# print(json.dumps(response.json(), indent=2))


response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]) #weezer


o = response.json()
for result in o["results"]:
  print(result["trackName"])