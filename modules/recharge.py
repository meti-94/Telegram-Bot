from commons import *


async def recharge(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text

    reply = """افزایش اعتبار را انتخاب کردی 💎

    برای خرید یک پکیج ده تایی از ایمیل 💼 100 هزارتومن به حساب شماره کارتی که ربات برات فرستاده 💳 به نام محمد مهدی جعفری واریز کن 💰 بعد فیش واریزتو بفرست 📤 برای آی دی 
    @applypro_admin
    در سریع ترین زمان ممکن پرداختت تأیید میشه ✅ و اعتبارت بروزرسانی میشه 🔄 بعد یک پیام از ادمین میگیری 📬 و میتونی مجدد از ربات استفاده کنی 🤖 
    """
    
    
    file_id = 'AgACAgQAAxkBAAIDJ2UR9aHp2V7ogXsDDsLEK0jr_CELAAKRvzEbg5CQULmRZdf6Ei6oAQADAgADeQADMAQ'
    await update.message.reply_photo(photo=file_id, caption="تصویر کارت 💳")

    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    
    return ConversationHandler.END
