from datetime import datetime, timedelta

from celery import shared_task

from django.core.mail import send_mail


@shared_task
def clear_logs():
    from teachers.models import Logger
    Logger.objects.filter(created__lt=datetime.now() - timedelta(days=7)).delete()


@shared_task
def send_message(email_from, title, message):
    message = f'Contact e-mail: {email_from}\nTitle: {title}\nMessage:\n{message}'
    send_mail(
        'Contact Us form message.',
        message,
        'koekuachu@ukr.net',
        ['dmytro.kaminskyi92@gmail.com'],
    )
