# Generated by Django 4.0.2 on 2022-03-02 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_address_alter_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
    ]
