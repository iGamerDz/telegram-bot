from telethon import TelegramClient, events
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

client = TelegramClient("session", api_id, api_hash)

CHANNEL = "kingxauusd1"

@client.on(events.NewMessage(chats=CHANNEL))
async def handler(event):
    msg = event.message.message.lower()

    if "حضور ... 🦅" in msg:
        await client.send_message("me", f"🚨 إشعار:\n\n{event.message.message}")

print("Bot running...")
client.start()
client.run_until_disconnected()