from commons import *

async def field(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text

    reply = """📘 حالا عنوان رشته تحصیلیت رو وارد کن. 🖊"""
    
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    INFO[c_id]['دانشگاه یا مؤسسه آموزشی'] = msg
    return APPLICANT
