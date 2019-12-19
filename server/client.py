from requests import put, get
import requests
date = {
    "month" : 1,
    "date" : 2
}
url = "http://127.0.0.1:5000/"
response = requests.post(url, data = date)
print(response.text)