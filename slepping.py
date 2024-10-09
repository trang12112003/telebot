from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from datetime import datetime
import asyncio

# Đặt giờ nhắc nhở
reminder_time = "22:00"  # Thay đổi thành giờ bạn muốn

async def remind(update: Update, context):
    current_time = datetime.now().strftime("%H:%M")
    if current_time == reminder_time:
        await update.message.reply_text("Đã đến giờ đi ngủ!")

async def start(update: Update, context):
    await update.message.reply_text(f"Bot nhắc đi ngủ vào lúc {reminder_time} đã được bật.")

if __name__ == '__main__':
    # Thêm API token của bạn vào đây
    app = ApplicationBuilder().token('7869617918:AAEAaEvnN3gOvRA7k9ZyTdh_KqeRm1qYiAs').build()

    # Lệnh /start để bật bot
    app.add_handler(CommandHandler("start", start))

    # Kiểm tra giờ liên tục để nhắc nhở
    async def check_time():
        while True:
            now = datetime.now().strftime("%H:%M")
            if now == reminder_time:
                print("Đã đến giờ đi ngủ!")
            await asyncio.sleep(60)  # Kiểm tra lại mỗi phút

    app.job_queue.run_repeating(remind, interval=60, first=0)

    # Chạy bot và hàm kiểm tra giờ
    app.run_polling()