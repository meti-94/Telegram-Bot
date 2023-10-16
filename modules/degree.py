from commons import *

async def degree(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    
    reply = f"""⚠️ حواست باشه ربات هنوز دارای توانایی ویرایش اطلاعات ثبت شده نیست پس بیشتر دقت کن! 👀"""
    
    reply_keyboard = [["🎓 کارشناسی", "👩‍🎓 کارشناسی ارشد", "👨‍🎓 دکترا"]]
    
    reply += f"""\n\nحالا میخوای برای کدوم مقطع ایمیل بزنی؟ 🤔"""
    
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, 
            one_time_keyboard=True, 
            input_field_placeholder="مقطع تحصیلی؟ 🎓",
        ),
        parse_mode=ParseMode.HTML
    )
    
    return PROFESSOR
