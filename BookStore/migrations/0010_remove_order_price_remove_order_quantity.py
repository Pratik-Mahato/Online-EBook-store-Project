# Generated by Django 4.2.3 on 2023-08-26 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0009_alter_order_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]
