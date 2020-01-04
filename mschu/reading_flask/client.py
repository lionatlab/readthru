import requests

date = {
    "month": 12,
    "day": 31
}
url = "http://127.0.0.1:5000/"
response = requests.post(url, data=date)
print(response.text)
