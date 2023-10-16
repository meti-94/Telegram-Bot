from commons import *

async def professor(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text

    reply = """
                📚 لطفاً اسم استادی که میخوای باهاش کار کنی رو به لاتین وارد کن.
                راستی 🤓 لازم نیست که دکتر یا پروفسور بهش اضافه کنی، ربات حواسش به این موضوع هست.
            """
    
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    INFO[c_id]['مقطع تحصیلی'] = msg.split(' ')[-1]
    
    return INSTITUTE
