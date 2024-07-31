from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from config.settings import EMAIL_HOST_USER
from dogs.models import Dog
from dogs.services import send_telegram_message
from users.models import User
# import requests

@shared_task
def send_information_about_like(email):
    """Отправляет сообщение пользователю о поставленном лайке"""
    message = "Вашей собаке только что поставили лайк"
    send_mail("Новый лайк", message, EMAIL_HOST_USER, (email,))
    user = User.objects.get(email=email)
    if user.tg_chat_id:
        send_telegram_message(user.tg_chat_id, message)


@shared_task
def send_email_about_birthday():
    today = timezone.now().today().date()
    dogs = Dog.objects.filter(owner__isnull=False, date_born=today)
    email_list = []
    message = "Поздравляем! У вашей собаки сегодня день рожденья!"
    for dog in dogs:
        email_list.append(dog.owner.email)
        if dog.owner.tg_chat_id:
            send_telegram_message(dog.owner.tg_chat_id, message)
    if email_list:
        print(email_list)
        send_mail(
            "У вашей собаки день рожденья!",
            message,
            EMAIL_HOST_USER,
            email_list
        )
    else:
        print("no emails sended today")
