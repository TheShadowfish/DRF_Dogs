from celery import shared_task
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.template.loader import render_to_string

@shared_task
def send_information_about_like(email):
    """Отправляет сообщение пользователю о поставленном лайке"""
    send_mail('Новый лайк', 'Вашей собаке поставили лайк', EMAIL_HOST_USER, (email,))
