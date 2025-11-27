import requests
import time

your_api_key = 'YOUR_API_KEY' # set to be equal to your_api_key from main.py
reciever_username = "@parolk06"

res = requests.post("http://0.0.0.0:8000/send", json={
    "username": reciever_username,
    "message": "test msg",
    "api_key": your_api_key,
})
print(res.json())

for i in range(5):
    res = requests.post("http://0.0.0.0:8000/send", json={
        "username": reciever_username,
        "message": "(" + str(i) + ")",
        "api_key": your_api_key,
    })
    time.sleep(4)
    print(res.json())
