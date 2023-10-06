import logging

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)



def send_email_with_html_body(subject: str, receivers: list, template:str, context:dict):
    """ This fonction help to send a customize email to a specific user or set of user """

    try:
        message = render_to_string(template, context)

        send_mail(
            subject,
            message,
            receivers,
            settings.EMAIL_HOST_USER,
            fail_silently=True,
            html_message=message
            )

    except Exception as e:
        logger.error(e)    

    return False    