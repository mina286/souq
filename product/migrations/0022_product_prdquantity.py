# Generated by Django 4.0.2 on 2022-02-28 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_alter_product_prdreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDquantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='الكميه فى المخزن '),
        ),
    ]
