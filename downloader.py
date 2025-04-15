from flask import Flask, abort, redirect
from helper.jsondb import get_file_info

app = Flask(__name__)
BOT_TOKEN = "5088657122:AAHdusGDuWfBpSDWkcX-qU1_fgzij4w8Lzk"

@app.route("/<file_id>")
def serve_file(file_id):
    file_info = get_file_info(file_id)
    if not file_info:
        return abort(404)
    tg_link = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_id}"
    return redirect(tg_link)

def start_flask():
    app.run(host="0.0.0.0", port=8080)
