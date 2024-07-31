from celery import shared_task
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


@shared_task
def send_information_about_like(email):
    """Отправляет сообщение пользователю о поставленном лайке"""
    send_mail('Новый лайк', 'Вашей собаке поставили лайк', EMAIL_HOST_USER, (email,))


@shared_task
def send_mail_about_birthday():
    today = timezone.now().today()
