from commons import *

async def institute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text

    reply = """🏫 لطفاً نام مؤسسه یا دانشگاه مربوطه رو به لاتین وارد کن. 📝"""
    
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    INFO[c_id]['نام استاد'] = msg
    return FIELD
