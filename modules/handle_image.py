from commons import *


async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Get the photo file_id from the message
    photo = update.message.photo[-1]  # photo is an array, get the highest resolution one
    file_id = photo.file_id
    
    # Print the file_id to the console
    logger.info("File ID:", file_id)
    await update.message.reply_text("Image received!")