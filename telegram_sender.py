import requests

TELEGRAM_BOT_TOKEN = "7716803670:AAGrCYHa_qObvQ_hAq2eelj2v18mCM86Yi0"
TELEGRAM_CHAT_ID = "7436059860"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Telegram message sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending Telegram message: {e}")


