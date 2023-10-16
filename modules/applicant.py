from commons import *

async def applicant(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text

    reply = """👤 حالا لطفاً اسم و فامیل خودت رو به لاتین وارد کن. 🖊"""
    
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    INFO[c_id]['رشته تحصیلی'] = msg
    return INTEREST
