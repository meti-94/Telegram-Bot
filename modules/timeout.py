from commons import *

async def timeout(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text

    reply = f"""⏳ ربات پس از {TIMEOUT_COUNT} ثانیه انتظار، مکالمه رو خاتمه داد. 😓"""
    
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    
    return ConversationHandler.END
