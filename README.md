# API Telegram sender Docs
This is a webserver that allows you to send messages to anybody in telegram from their username (@username).\
It is built for **LINUX**, but should also work on macos.

```bash
git clone https://github.com/yaroslav-06/api_telegram_sender.git && cd api_telegram_sender
```
## Setup
Go to [https://my.telegram.org/](https://my.telegram.org/), login with your telegram accound, and get "App api_id", and "App api_hash".

Open *main.py* file and paste your api id, and api hash in corresponding variables (id as an int, hash as a string).
Also insert random string into _your_api_key_ variable, this will be your password for future access.

>[!IMPORTANT]
>If you are running for the first time Telegram will force you to login, so first time you should run:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

And follow the telegram setup steps.\
(exit with ctrl-c after setup)

## Running
To start the server on background run: 
```bash
nohup uvicorn main:app --host 0.0.0.0 --port 8000 > log.txt 2>&1 &
```

> [!WARNING]
> Since we aren't using any encryption, all messages (and even your_api_key) can be readable to anyone in between client and server.

## Testing
To test run: 
```bash
python3 test.py
```
And follow the promt instructions.

It should send 6 messages to you.
