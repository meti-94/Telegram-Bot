from commons import *


async def guide(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    c_id = update.message.chat_id
    msg = update.message.text

    reply = """&#x202b;سلام &#x1F31F;&#x1F31F;
این راهنمای استفاده از ربات <b><i>ApplyPro</i></b> هست که بدست شما رسیده &#x1F916;&#x1F4D8;
این پست یک <b><i>فیلم آموزشی</i></b> دارد &#x1F3A5; که تعامل کاربر با ربات را نشان میدهد. همچنین، اطلاعاتی که در فیلم وارد شد و متن ایمیل نیز برای تحلیل دقیقتر ارسال شده است &#x1F4E9;&#x1F50D;
بدین وسیله از شما دعوت میشود که با استفاده از <b><i>اعتبار اولیه حسابتان</i></b>، اولین <b><i>ایمیل شخصی سازی شده و حرفه ای</i></b> خودتان را بنویسید &#x2709;&#xFE0F;&#x1F31E;
توجه داشته باشید که ربات دارای قابلیت <b><i>ترجمه دقیق</i></b> جملات و عبارت ها هست اما برای وارد کردن مواردی نظیر نام ها بایستی از <b><i>زبان لاتین</i></b> استفاده کنید. &#x1F310;
سایر قسمت ها نیز در صورت لزوم میتوانند به زبان انگلیسی وارد شوند منوط به این که کاربر ترجمه دقیق و صحیح ارائه دهد. &#x1F1EC;&#x1F1E7;
<b>روبات اپلای پرو</b> | 


@applypro_bot &#x1F680;
"""
    
    
    await update.message.reply_text(
        reply,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    
    file_id = 'CgACAgQAAxkBAAIEGWUVMX7yyFawknZJCJaoxIuspqftAAJQEgACrqKhUMY20bFhbZxrMAQ'
    await update.message.reply_animation(animation=file_id, caption="🤖 انیمیشن راهنمای استفاده از ربات @applypro_bot 📚✅")
    


    reply = """"📌 <strong><em>تمام اطلاعاتی که ربات از کاربر دریافت کرد</em></strong>
        👇👇👇
        
        🎓 <strong><em>مقطع تحصیلی</em></strong> ⬇️
        🔸 دکترا 
        
        👨‍🏫 <strong><em>نام استاد</em></strong> ⬇️
        🔸 Barney May 
        
        🏢 <strong><em>دانشگاه یا مؤسسه آموزشی</em></strong> ⬇️
        🔸 دانشکده علوم کامپیوتر در دانشگاه آکسفورد 
        
        📘 <strong><em>رشته تحصیلی</em></strong> ⬇️
        🔸 مهندسی کامپیوتر 
        
        👤 <strong><em>نام متقاضی</em></strong> ⬇️
        🔸 Mina Rahmati 
        
        🔬 <strong><em>علایق پژوهشی متقاضی</em></strong> ⬇️
        🔸 پردازش زبان طبیعی و یادگیری ماشین توضیح پذیر 
        
        📜 <strong><em>تجربیات کاری و آکادمیک</em></strong> ⬇️
        🔸 یک مقاله کنفرانسی، دو مقاله ژورنالی و دوبار دستیاری استاد در درس یادگیری ماشین 
        
        📄 <strong><em>موارد ضمیمه شده</em></strong> ⬇️
        🔸 کارنامه های کارشناسی و کارشناسی ارشد، رزومه
        
        📧 متن و عنوان پیشنهادی برای ایمیل
        👇👇👇
        
        <b>روبات اپلای پرو</b> | 


        @applypro_bot &#x1F680;
        """
    await update.message.reply_text(
        reply,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    reply = """Subject: Inquiry for Doctorate Studies in Computer Engineering at the University of Oxford 

Dear Professor Barney May,

I hope this email finds you well. My name is Mina Rahmati, and I am fervently interested in pursuing a Doctorate in Computer Engineering at the University of Oxford, specifically at the Faculty of Computer Science where your esteemed presence and contributions are well-recognized.

My key research interests lie in Explainable Machine Learning and Natural Language Processing. I am excited about the potential opportunity of collaborating with you. My research experiences include a conference paper, two journal articles and two instances where I was an assistant to a professor in a Machine Learning course.

The various documents attached include my undergraduate and graduate transcripts, as well as my CV to provide a comprehensive review of my academic achievements and ongoing research pursuits.

I am looking forward to further discussing potential opportunities to collaborate and how I might be able to contribute to your ongoing research.

Thank you for considering my application. I am anticipating our potential collaboration at Oxford.

Yours sincerely,
Mina Rahmati.

<b>روبات اپلای پرو</b> | 


@applypro_bot &#x1F680;
"""
    await update.message.reply_text(
        reply,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )


    return ConversationHandler.END