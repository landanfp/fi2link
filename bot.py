
import json
import string
import random
from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
LOG_CHANNEL = -1001792962793

app = Client("file2link-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def generate_token(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def load_files():
    if not os.path.exists("files.json"):
        return {}
    with open("files.json", "r") as f:
        return json.load(f)

def save_files(data):
    with open("files.json", "w") as f:
        json.dump(data, f, indent=2)

@app.on_message(filters.document | filters.video)
async def handle_file(client, message: Message):
    file = message.document or message.video
    sent = await file.copy(LOG_CHANNEL)
    token = generate_token()
    expires_at = "never"

    data = load_files()
    data[token] = {
        "file_id": file.file_id,
        "message_id": sent.id,
        "channel_id": LOG_CHANNEL,
        "file_name": file.file_name,
        "expires_at": expires_at
    }
    save_files(data)

    link = f"https://obnoxious-nichole-farsa-1880b732.koyeb.app/dl/{token}"
    await message.reply(f"✅ لینک دانلود فایل:
{link}

لینک دائمی است تا زمانی که فایل از کانال حذف نشود.")

app.run()
