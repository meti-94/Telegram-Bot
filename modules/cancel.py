from commons import *

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    
    reply = """🚫 شما درخواستتان را کنسل کردید، امیدواریم در مسیر اپلای خودتون موفق باشید. 🌟
                
                دوباره به ما سر بزنید 🚪 چون قرار هست خدماتمون رو پیوسته ارتقاء بدیم. 🚀
                """
    
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    INFO.pop(c_id)
    return ConversationHandler.END
