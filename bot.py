from pyrogram import Client
from database.ia_filterdb import Media
from database.users_chats_db import db


PyrogramBot = Client(
    "ADV GUARDIAN GROOT",
    api_hash="5023c40ea655bc2834e48888b17ccee8", 
    api_id="13160306", 
    bot_token="5221793107:AAGzaFdLJoZIBmKB1MeOLJCJRfK0rFfYkVg", 
    plugins=dict(root="ADV_GUARDIAN_GROOT")
)






PyrogramBot.run()
