import os
from requests import Response, post

class MailgunException(Exception):
    def __init__(self, message):
        self.message = message


class Mailgun:

    FROM_TITLE = 'VIL'
    FROM_EMAIL = 'no-responder@sandbox4d7dc19be3cf4dc78d09d5b693de9bc8.mailgun.org'

    @classmethod
    def send_mail(cls, email, subject, text, html):
        MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY', None)
        MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN', None)
        if MAILGUN_API_KEY is None:
            raise MailgunException('Failed to load Mailgun API')

        if MAILGUN_DOMAIN is None:
            raise MailgunException('Failed to load Mailgun domain')

        response = post(f"{MAILGUN_DOMAIN}/messages",
		    auth=("api", MAILGUN_API_KEY),
		    data={"from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
			      "to": email,
			      "subject": subject,
			      "text": text,
                  "html": html
                  })
        if response.status_code != 200:
            raise MailgunException("Hubo un error al enviar el email.")
        return response


