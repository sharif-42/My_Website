from applibs.email_services import EmailServices


class SendMailService:
    def __init__(self):
        self.to = 'sharifulcsehstu@gmail.com'  # TODO: set this value in settings.py

    def send_email(self, data):
        name = str(data.get('first_name')) + ' ' + str(data.get('last_name'))
        email = data.get('email')
        html_content = 'Name: <strong>{}</strong></p><p>Email: <strong>{}</strong></p><p>Phone:<strong>{}</strong></p>' \
            .format(name, email, data.get('telephone_number'))
        email = EmailServices(subject="contact me", html_content=html_content,email=email)
        res_code , response = email.send_mail()

