# Generated by Django 4.0.2 on 2022-02-27 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_product_prdslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDslug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, verbose_name='slug'),
        ),
    ]
