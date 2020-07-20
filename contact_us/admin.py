from django.contrib import admin

from contact_us.models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    """
        This class is used to show admin interface for
        Contact Us.
        """
    list_display = ('id', 'first_name', 'telephone_number', 'email', 'submitted', 'message')


admin.site.register(ContactUs, ContactUsAdmin)
