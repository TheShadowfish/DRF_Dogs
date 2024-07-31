from celery import shared_task
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from dogs.models import Dog


@shared_task
def send_information_about_like(email):
    """Отправляет сообщение пользователю о поставленном лайке"""
    send_mail('Новый лайк', 'Вашей собаке поставили лайк', EMAIL_HOST_USER, (email,))


@shared_task
def send_email_about_birthday():
    today = timezone.now().today().date()
    dogs = Dog.objects.filter(owner__isnull=False, date_born=today)
    email_list = []
    for dog in dogs:
        email_list.append(dog.owner.email)
    if email_list:
        print(email_list)
    else:
        print("no emails sended today")
