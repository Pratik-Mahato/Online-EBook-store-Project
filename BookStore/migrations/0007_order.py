# Generated by Django 4.2.3 on 2023-08-25 15:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0006_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('Books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookStore.books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookStore.user')),
            ],
        ),
    ]
