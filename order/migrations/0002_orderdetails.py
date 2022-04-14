# Generated by Django 4.0.2 on 2022-03-10 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_product_free_shipping'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ODquantity', models.IntegerField(verbose_name=' الكمية')),
                ('ODprice', models.DecimalField(decimal_places=2, max_digits=9, verbose_name=' السعر')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name=' الاورد')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name=' المنتج')),
            ],
        ),
    ]