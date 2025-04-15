from pyrogram import Client
from bot import setup_handlers
from downloader import start_flask
import threading

api_id = 3335796 
api_hash = "138b992a0e672e8346d8439c3f42ea78"
bot_token = "7136875110:AAFzyr2i2FbRrmst1sklkJPN7Yz2rXJvSew"

app = Client("file2link_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
setup_handlers(app)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()
    app.run()
