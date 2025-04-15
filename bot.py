from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helper.jsondb import save_file_info

LOG_CHANNEL = -1001792962793
WEB_DOMAIN = "https://obnoxious-nichole-farsa-1880b732.koyeb.app"

def setup_handlers(app):
    @app.on_message(filters.document | filters.video | filters.audio)
    async def handle_file(client, message: Message):
        sent = await message.copy(LOG_CHANNEL)
        file_id = str(sent.id)
        file_name = message.document.file_name if message.document else message.video.file_name or "file"
        save_file_info(file_id, file_name)
        link = f"{WEB_DOMAIN}/{file_id}"
        await message.reply(
            f"فایل شما آپلود شد!\n\nلینک دانلود:\n{link}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("دانلود", url=link)]])
        )
