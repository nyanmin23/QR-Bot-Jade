import qrcode
import logging
import io
import os  # For environment variables
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from qrcode.exceptions import DataOverflowError  # Import the specific error

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


# start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_html(
        f"Hi {update.effective_user.mention_html()}! I'm a QR code bot. Just send me any text."
    )


# help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        "This bot generates QR codes from the text you send. Just send any text and I'll reply with a QR code image."
    )


# QR code generation handler
async def generate_qr(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Generate a QR code from the user's message and send it as a photo."""
    text = update.message.text
    logger.info(
        f"Generating QR code for text of length {len(text)} from user {update.effective_user.id}"
    )

    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=None,  # Let the library choose the version automatically
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to an in-memory buffer
        img_buffer = io.BytesIO()
        img.save(img_buffer, "PNG")
        img_buffer.seek(0)  # Rewind the buffer to the beginning

        # Send the image from the buffer with a caption
        await update.message.reply_photo(
            photo=img_buffer, caption="✅ QR Code generated successfully!"
        )

    except DataOverflowError:
        # Handle cases where the text is too long
        logger.warning(f"Data overflow for text: {text}")
        await update.message.reply_text(
            "⚠️ The text you sent is too long to fit in a QR code. Please try a shorter text."
        )


def main() -> None:
    """Start the bot."""

    # Load environment variables from .env file
    load_dotenv()

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set!")
        return

    # Create the Application and pass in bot's token.
    application = Application.builder().token(token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Use the new function name
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, generate_qr)
    )

    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
