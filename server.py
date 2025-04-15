
import json
import requests
from flask import Flask, abort, redirect
from datetime import datetime
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
CDN_URL = f"https://api.telegram.org/file/bot{BOT_TOKEN}"

app = Flask(__name__)

def load_files():
    try:
        with open("files.json", "r") as f:
            return json.load(f)
    except:
        return {}

@app.route("/dl/<token>")
def serve_file(token):
    data = load_files().get(token)
    if not data:
        return "❌ لینک نامعتبر است یا وجود ندارد.", 404

    # بررسی انقضا
    if data["expires_at"] != "never" and datetime.utcnow() > datetime.fromisoformat(data["expires_at"]):
        return "⏳ لینک منقضی شده است.", 410

    # بررسی وجود فایل در کانال
    resp = requests.get(f"{API_URL}/getMessage", params={
        "chat_id": data["channel_id"],
        "message_id": data["message_id"]
    })
    if not resp.ok or not resp.json().get("ok"):
        return "❌ فایل از کانال حذف شده است.", 410

    # دریافت لینک فایل
    file_resp = requests.get(f"{API_URL}/getFile", params={"file_id": data["file_id"]})
    if not file_resp.ok:
        return "❌ دریافت فایل با خطا مواجه شد.", 500

    file_path = file_resp.json()["result"]["file_path"]
    return redirect(f"{CDN_URL}/{file_path}", code=302)
