from commons import *

async def interest(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text

    reply = """🔍 حالا علایق پژوهشیت رو وارد کن، باید قبلاً چک کرده باشی که با زمینه های پژوهشی استاد مورد علاقت سازگار باشه. 📚"""
    
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    INFO[c_id]['نام متقاضی'] = msg
    return EXPERIENCE
