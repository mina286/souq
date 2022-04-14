# Generated by Django 4.0.2 on 2022-03-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_address_is_friday_alter_address_is_home_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Building_name_or_number',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='اسم/رقم المبنى، رقم الطابق، رقم الشقة، أو رقم الفيلا'),
        ),
        migrations.AlterField(
            model_name='address',
            name='Governorate',
            field=models.CharField(max_length=150, verbose_name='المحافظة'),
        ),
        migrations.AlterField(
            model_name='address',
            name='Region',
            field=models.CharField(max_length=150, verbose_name='المنطقة/المدينة'),
        ),
        migrations.AlterField(
            model_name='address',
            name='Street_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='اسم الشاع'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=150, verbose_name='البلد'),
        ),
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='الحى'),
        ),
        migrations.AlterField(
            model_name='address',
            name='is_friday',
            field=models.BooleanField(blank=True, null=True, verbose_name='الجمعة'),
        ),
        migrations.AlterField(
            model_name='address',
            name='is_home',
            field=models.BooleanField(blank=True, null=True, verbose_name='المنزل'),
        ),
        migrations.AlterField(
            model_name='address',
            name='is_main_address',
            field=models.BooleanField(blank=True, null=True, verbose_name='عنوان ئيسي'),
        ),
        migrations.AlterField(
            model_name='address',
            name='is_starday',
            field=models.BooleanField(blank=True, null=True, verbose_name='السبت'),
        ),
        migrations.AlterField(
            model_name='address',
            name='is_work',
            field=models.BooleanField(blank=True, null=True, verbose_name='العمل'),
        ),
        migrations.AlterField(
            model_name='address',
            name='nearest_mark',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='أقرب علامة مميزة'),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.IntegerField(verbose_name='رقم الموبيل'),
        ),
    ]