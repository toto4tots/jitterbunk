# Generated by Django 2.1 on 2022-06-16 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunks', '0005_auto_20220616_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
    ]