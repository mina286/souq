# Generated by Django 4.0.2 on 2022-02-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDname', models.CharField(max_length=100, verbose_name='اسم المنتج')),
                ('PRDdesc', models.TextField(verbose_name='وصف المنتج')),
                ('PRDprice', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='السعر ')),
                ('PRDcost', models.DecimalField(decimal_places=2, max_digits=9, verbose_name=' التكلفه')),
                ('PRDcreated', models.DateTimeField(verbose_name=' وقت اضافة المنتج')),
            ],
        ),
    ]
