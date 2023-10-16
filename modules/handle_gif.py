from commons import *

async def handle_gif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Check if the incoming message contains a GIF (animation)
    if update.message.animation:
        # Get the animation file_id from the message
        animation = update.message.animation
        file_id = animation.file_id
        
        # Print the file_id to the console
        logger.info(f"File ID: {file_id}")
        await update.message.reply_text("GIF received!")
    else:
        await update.message.reply_text("That is not a GIF!")
    return ConversationHandler.END
