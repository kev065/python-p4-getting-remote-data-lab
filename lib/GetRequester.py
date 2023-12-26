import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):     
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        jsonified = json.loads(self.get_response_body())
        return jsonified

url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

site = GetRequester(url)
print(site.load_json())