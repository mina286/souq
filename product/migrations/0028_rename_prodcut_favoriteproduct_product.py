# Generated by Django 4.0.2 on 2022-03-12 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_favoriteproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoriteproduct',
            old_name='prodcut',
            new_name='product',
        ),
    ]