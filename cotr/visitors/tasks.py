from flask_mail import Message

from cotr import celery, mail

@celery.task
def send_mail(subject, recipients, content):
    msg = Message(subject=subject,
                  recipients=recipients,
                  html=content)
    mail.send(msg)

