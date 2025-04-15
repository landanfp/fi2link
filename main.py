from pyrogram import Client
from bot import setup_handlers
from downloader import start_flask
import threading

api_id = 1234567
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"

app = Client("file2link_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
setup_handlers(app)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()
    app.run()