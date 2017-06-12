from flask_mail import Message

from cotr import mail
from cotr.celery import app as celery

@celery.task
def send_mail(subject, recipients, content):
    msg = Message(subject=subject,
                  recipients=recipients,
                  html=content)
    mail.send(msg)

