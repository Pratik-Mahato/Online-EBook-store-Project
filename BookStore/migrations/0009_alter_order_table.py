# Generated by Django 4.2.3 on 2023-08-26 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0008_rename_books_order_book_rename_user_order_customer'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
    ]
