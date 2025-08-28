from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ContextTypes, MessageHandler, filters

# Token bot kamu
TOKEN = "7733855200:AAE_sMrHx83o_Ip9bX7btinZmyKax7D3elA"

# Inline keyboard promo
def get_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Subcribe Channel", url="https://t.me/afb88my")],
        [InlineKeyboardButton("📢 Group Cuci&Tips GAME", url="https://t.me/+b685QE242dMxOWE9")],
        [InlineKeyboardButton("📢 Promotion", url="https://t.me/Veronica88bot")],
    ])

# Balasan promo (hanya tombol)
async def send_promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "📌 Pilih menu di bawah:",
            reply_markup=get_keyboard()
        )

# Handler: hanya respon postingan admin
async def admin_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user

    # Ambil daftar admin
    admins = await chat.get_administrators()
    admin_ids = [admin.user.id for admin in admins]

    # Jika pengirim admin → kirim balasan tombol
    if user and user.id in admin_ids:
        await send_promo(update, context)

def main():
    app = Application.builder().token(TOKEN).build()

    # Handler: semua jenis pesan di grup, tapi hanya dari admin
    app.add_handler(MessageHandler(filters.ALL & filters.ChatType.GROUPS, admin_post))

    print("🤖 Bot sudah jalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
