# Generated by Django 4.0.2 on 2022-02-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_prdimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDslug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
    ]
