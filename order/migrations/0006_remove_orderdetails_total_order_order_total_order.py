# Generated by Django 4.0.2 on 2022-03-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_orderdetails_total_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='total_order',
        ),
        migrations.AddField(
            model_name='order',
            name='total_order',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name=' مجمل الاورد'),
        ),
    ]
