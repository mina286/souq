# Generated by Django 4.0.2 on 2022-02-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_product_prdimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDimage',
            field=models.ImageField(upload_to='product_photo/%Y/%m/%d/', verbose_name='الصوره الرئيسية للمنتج'),
        ),
    ]