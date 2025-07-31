# QR Bot Jade

#### Video Demo: https://youtu.be/JKlTCOoEadA?si=veHovSA6skGKUJTX
#### Description:

`QR Bot Jade`, a final project for `CS50x`, is a Telegram bot that generates QR codes from user input. The project’s architecture revolves around the `QRbot.py` script, which encapsulates the application’s complete logic. This script utilizes the `python-telegram-bot` library for asynchronous communication with the `Telegram Bot API`, employing `CommandHandler` and `MessageHandler` to route user input to appropriate functions.

The core functionality is powered by the `qrcode` library, which processes user text to compute QR code data. This data is subsequently rendered into a PNG image using the `Pillow` library (a dependency of `qrcode`) and transmitted back to the user as an in-memory BytesIO object to avoid disk writing. To mitigate potential issues, the code specifically catches the `DataOverflowError` from the `qrcode` library, enabling the bot to inform users if their input exceeds the QR code’s capacity.

Project configuration and security are managed through several key files. The `requirements.txt` file lists all necessary `Python` packages, including `python-telegram-bot` and `qrcode`, ensuring that the project’s environment can be precisely replicated using `pip`. Sensitive information, specifically the `TELEGRAM_BOT_TOKEN`, is loaded at runtime from a local `.env` file using the `python-dotenv` library. This practice is enforced by the `.gitignore` file, which prevents the `.env` file from being committed to version control, thereby safeguarding secret credentials. These components collectively contribute to a robust, secure, and efficient application.


---

## Features

* **Direct QR Code Generation**: Converts any text message directly into a QR code.
* **`/start` Command**: Welcomes the user and provides a brief introduction to the bot.
* **`/help` Command**: Offers simple instructions on how to use the bot.
* **Error Handling**: Notifies the user if the provided text is too long to be converted into a QR code.
* **Secure Token Management**: Uses a `.env` file to securely manage the Telegram Bot API token.

---

## How to Set Up and Run the Project

To get this project running on your local machine, follow these steps:

### 1. Prerequisites

* Python 3.8 or higher
* A Telegram account
* A Telegram Bot Token (get one from [BotFather](https://t.me/botfather))


### 2. Installation
First, clone the repository to your local machine:

1.  **Clone the repository:**
```bash
git clone https://github.com/nyanmin23/QR-Bot-Jade.git
cd QR-Bot-Jade
```

2.  **Set up a virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate
```
**On Windows:**
```bash
.venv\Scripts\activate
```

3.  **Install dependencies:**
```bash
pip install -r requirements.txt
```

4.  **Create `.env` file** and add your token:
```
TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN_HERE"
```

5.  **Run the bot:**
```bash
python QRbot.py
```