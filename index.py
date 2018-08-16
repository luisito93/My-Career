import json
import requests
class call_api(url):
    response = requests.get(url)
    data = json.loads(response.content.decode('utf-8'))

    def fun(url):
        print(data[0]['title'])

fun("localhost:8000/api/jobs/3")