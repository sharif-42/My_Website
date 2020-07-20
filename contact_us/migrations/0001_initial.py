# Generated by Django 3.0.7 on 2020-07-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(help_text='Company Name.', max_length=100)),
                ('first_name', models.CharField(help_text='First name.', max_length=100)),
                ('last_name', models.CharField(help_text='Last name.', max_length=100)),
                ('telephone_number', models.CharField(help_text='Telephone number or contact number.', max_length=20)),
                ('email', models.EmailField(help_text='Email Address.', max_length=254)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('submitted', models.BooleanField(default=False)),
            ],
        ),
    ]
