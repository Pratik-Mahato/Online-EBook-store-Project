# Generated by Django 4.2.3 on 2023-08-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0010_remove_order_price_remove_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]