# Generated by Django 2.1 on 2022-06-16 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunks', '0004_bunk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 0, 29, 13, 179136), verbose_name='date'),
        ),
    ]
