
from modules.recharge import *
from modules.guide import *
from modules.start import *
from modules.degree import *
from modules.professor import *
from modules.institute import *
from modules.field import *
from modules.applicant import *
from modules.interest import *
from modules.experience import *
from modules.attachment import *
from modules.writing import *
from modules.cancel import *
from modules.timeout import *
from modules.handle_image import *
from modules.handle_gif import *




def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Add conversation handler with the states DEGREE, PROFESSOR, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING:   [
                            MessageHandler(filters.Regex("^(✉️ نوشتن ایمیل)$") & (~ filters.COMMAND), degree),
                            MessageHandler(filters.Regex("^(💰 افزایش اعتبار)$") & (~ filters.COMMAND), recharge),
                            MessageHandler(filters.Regex("^(📘 دریافت راهنما)$") & (~ filters.COMMAND), guide),
                        ],
            PROFESSOR:  [MessageHandler(filters.TEXT & (~ filters.COMMAND), professor)],
            INSTITUTE:  [MessageHandler(filters.TEXT & (~ filters.COMMAND), institute)],
            FIELD:      [MessageHandler(filters.TEXT & (~ filters.COMMAND), field)],
            APPLICANT:  [MessageHandler(filters.TEXT & (~ filters.COMMAND), applicant)],
            INTEREST:   [MessageHandler(filters.TEXT & (~ filters.COMMAND), interest)],
            EXPERIENCE: [MessageHandler(filters.TEXT & (~ filters.COMMAND), experience)],
            ATTACHMENT: [MessageHandler(filters.TEXT & (~ filters.COMMAND), attachment)],
            WRITING:    [MessageHandler(filters.TEXT & (~ filters.COMMAND), writing)],
            TIMEOUT:    [MessageHandler(filters.TEXT & (~ filters.COMMAND), timeout)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        conversation_timeout=TIMEOUT_COUNT,
    )

    application.add_handler(conv_handler)
    # image_handler = MessageHandler(filters.PHOTO, handle_image)
    # application.add_handler(image_handler)
    # gif_handler = MessageHandler(filters.ANIMATION, handle_gif)
    # application.add_handler(gif_handler)
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

