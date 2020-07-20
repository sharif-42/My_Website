from django.core.mail import EmailMessage


class EmailServices:
    """
    This Class is responsible for all kinds of email send related job.
    """
    def __init__(self, subject, html_content, email, to=None, attachment=None):
        self.subject = subject
        self.html_content = html_content,
        self.email = email
        self.to = ['sharifulcsehstu@gmail.com']  # TODO: set this value in settings.py
        self.attachment = attachment

    def send_mail(self):
        email = EmailMessage(
            subject=self.subject,
            body=self.html_content,
            from_email=self.email,
            to=self.to,
        )
        email.content_subtype = "html"
        try:
            response = email.send()
            return 200, response
        except Exception as e:
            response = str(e)
            return 400, response
