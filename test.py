import requests
import time

your_api_key = input('enter your api key (from your_api_key variable in main.py): ')
reciever_username = input("enter username to which you want to send the message: ")

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
