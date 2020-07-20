from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContactUsManager(models.Manager):
    def create_contact(self):
        pass


class ContactUs(models.Model):
    first_name = models.CharField(
        max_length=100,
        help_text=_('First name.'),
    )
    last_name = models.CharField(
        max_length=100,
        help_text=_('Last name.'),
        blank=True,
        null=True
    )
    telephone_number = models.CharField(
        max_length=20,
        help_text=_('Telephone number or contact number.'),
    )
    email = models.EmailField(
        help_text=_('Email Address.')
    )
    message = models.TextField(
        help_text=_('User message to us.'),
    )
    submitted = models.BooleanField(
        default=False,
        help_text=_('Is Submitted?')
    )
    date_created = models.DateTimeField(auto_now_add=True)
    objects = ContactUsManager()

    def __str__(self):
        return str(self.email) + '-' + str(self.telephone_number)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

