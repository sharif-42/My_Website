# Generated by Django 3.0.7 on 2020-07-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0003_auto_20200720_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(help_text='User message to us.'),
        ),
    ]
