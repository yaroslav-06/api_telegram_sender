from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from telethon import TelegramClient
from contextlib import asynccontextmanager

# === Telegram credentials ===
session_name = 'anon_session'

telegram_api_id = 00000000 # 8-digit code from https://my.telegram.org/ -> API development tools
api_hash = 'TELEGRAM_API_HASH' # 32-symbol hex: api hash from https://my.telegram.org/ -> API development tools

your_api_key = 'CREATE_YOUR_API_KEY' # this is your password that is required to execute the send command

# === Lifespan handler to start TelegramClient ===
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.client = TelegramClient(session_name, telegram_api_id, api_hash)
    await app.state.client.start()
    print("✅ Telegram client started.")
    yield
    await app.state.client.disconnect()
    print("🛑 Telegram client stopped.")

# === Initialize FastAPI with lifespan ===
app = FastAPI(lifespan=lifespan)

# === Request body ===
class MessageRequest(BaseModel):
    username: str  # like "@pavlo"
    message: str
    api_key: str

@app.post("/send")
async def send_message(req: MessageRequest, request: Request):
    username = req.username.lstrip("@")
    message = req.message
    if req.api_key != your_api_key:
        raise HTTPException(status_code=401, detail="wrong api key")

    client: TelegramClient = request.app.state.client

    try:
        user = await client.get_entity(username)
        await client.send_message(user, message)
        return {"status": "success", "sent_to": f"@{username}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
