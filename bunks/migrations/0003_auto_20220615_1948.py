# Generated by Django 2.1 on 2022-06-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunks', '0002_auto_20220615_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.CharField(default='https://pbs.twimg.com/profile_images/3403341918/71c895ce6b9f016a0381eadfa2738f27_400x400.png', max_length=200),
        ),
    ]
