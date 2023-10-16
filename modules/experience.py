from commons import *

async def experience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text

    reply = """🌟 اگر قبلاً تجربه آکادمیک یا کاری شاخصی داشتی که دوست داری در ایمیل ذکر کنی اونو وارد کن. 🎓"""
    
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    INFO[c_id]['علایق پژوهشی متقاضی'] = msg
    return ATTACHMENT
