# QR Bot Jade

#### Video Demo: https://youtu.be/JKlTCOoEadA?si=veHovSA6skGKUJTX
#### Description:

This project is a simple Telegram bot created for the CS50x final project. The bot, named 'QR Bot Jade', generates QR codes from any text message/ link a user sends to it. It's built using Python and the `python-telegram-bot` library. The primary goal of this project was to explore the development of Telegram bots, handle asynchronous operations, and work with external APIs and libraries to create a practical and interactive application.

The bot is designed to be user-friendly. Upon receiving a text message, it instantly converts the text into a QR code image and sends it back to the user. It includes basic command handlers for `/start` and `/help` to guide new users. It also incorporates error handling for cases where the input text is too long to be encoded in a standard QR code.

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
```bash
git clone https://github.com/nyanmin23/QR-Bot-Jade.git
cd QR-Bot-Jade
python -m venv .venv
source .venv/bin/activate
pip install -r requirments.txt
python QRbot.py
