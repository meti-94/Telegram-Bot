from commons import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    f_name = update.message.chat.first_name
    l_name = update.message.chat.last_name
    u_name = update.message.chat.username
    

    user = db.get_user(c_id)
    does_exist = bool(user!=None)
    if not does_exist:
        db.add_user(
          u_name, 
          c_id, 
          f_name,
          l_name,
          INITIAL_CREDIT,
          INITIAL_MONEY)
    user = db.get_user(c_id)
    if does_exist and (user[5]>0):
        reply = f'''سلام 🌟
        {user[0]}
        خوشحالیم که دوباره به ربات اپلای پرو سر زدی 🎉، اعتبارت در این لحظه برابر با 
        {user[5]} ✨
        درخواست نگارش هست.'''
        reply_keyboard = [["✉️ نوشتن ایمیل", "💰 افزایش اعتبار", "📘 دریافت راهنما"]]
    elif does_exist and (user[5]<=0):
        reply = f'''سلام 😊
        {user[0]}
        خوشحالیم که دوباره به ربات اپلای پرو سر زدی، الان اعتبارت برای نوشتن ایمیل کافی نیست. 😢
        '''
        reply_keyboard = [["💰 افزایش اعتبار", "📘 دریافت راهنما"]]
    else:
        reply = f'''سلام 🌟
        {user[0]}
        به ربات اپلای پرو خوش اومدی 🎊، اعتبارت در این لحظه برابر با 
        {user[5]} ✨
        درخواست نگارش هست.'''
        reply_keyboard = [["✉️ نوشتن ایمیل", "💰 افزایش اعتبار", "📘 دریافت راهنما"]]

    await update.message.reply_text(
        f'<b dir="rtl">{reply}</b>',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, 
            one_time_keyboard=True, 
            input_field_placeholder="حالا چطور میتونم بهت کمک کنم؟ 🤔",
        ),
        parse_mode=ParseMode.HTML
    )
    
    INFO[c_id] = {}


    return CHOOSING
