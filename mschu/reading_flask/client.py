import requests

date = {
    "month": 1,
    "day": 2
}
url = "http://127.0.0.1:5000/"
response = requests.post(url, data=date)
print(response.text)
