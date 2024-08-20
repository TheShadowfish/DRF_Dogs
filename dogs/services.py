from config import settings
import requests
def send_telegram_message(chat_id, message):
    """Функция отправки сообщения в телеграм"""
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    print(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage')
    requests.get(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage', params=params)
    # response = requests.get(f'https://api.telegram.org/bot/{settings.TELEGRAM_TOKEN}/sendMessage', params=params)
