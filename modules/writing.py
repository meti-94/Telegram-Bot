from commons import *

async def writing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text
    u_name = update.message.chat.username

    reply = """📝 حالا که تمام اطلاعات مربوط به ایمیل شما دریافت شد، کار نگارش شروع میشه! """
    reply += """✅ این هم اطلاعاتی است که ربات از شما دریافت کرد:"""
    INFO[c_id]['موارد ضمیمه شده'] = msg

    for k, v in INFO[c_id].items():
        reply += f"\n {k} \t ⬇️\n {v} "

    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    reply = """🎉 ایمیل شما آماده است!"""
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    INFO[c_id]['مقطع تحصیلی'] = degree_mapping[INFO[c_id]['مقطع تحصیلی']]
    reply = writing_email(INFO[c_id])
    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )

    reply = """🌟 حواست باشه حتماً حتماً قبل از ارسال یکبار دیگه بخونی ایمیل رو! در ضمن، امیدواریم این آخرین ایمیلی باشه که برای پیدا کردن پزیشن ارسال میکنی :) """
    user = db.get_user(c_id)
    db.update_user(user[1], 'credit', user[5] - 1)
    return ConversationHandler.END

