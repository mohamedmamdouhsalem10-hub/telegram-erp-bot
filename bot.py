import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

FAQ = {
    "فاتورة": "لعمل فاتورة: Sales → Sales Invoice → New",
    "مستخدم": "لإضافة مستخدم: Settings → User → New",
    "صلاحية": "لتعديل الصلاحيات: Role Permission Manager",
    "تقرير": "التقارير داخل كل Module"
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    for key in FAQ:
        if key in text:
            await update.message.reply_text(FAQ[key])
            return

    await update.message.reply_text("تم تحويل طلبك للدعم الفني")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
