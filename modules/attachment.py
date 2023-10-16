from commons import *

async def attachment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text

    reply = """📎 اسم مدارکی که قرار هست به ایمیل پیوست کنی را وارد کن، اغلب اساتید دوست دارن رزومه، کارنامه تحصیلی و مقالات قبلی شمارو ببینند 📘📄"""
    
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    INFO[c_id]['تجربیات کاری و آکادمیک'] = msg
    return WRITING
