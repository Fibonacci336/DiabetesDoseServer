# Generated by Django 4.0.4 on 2022-05-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_user_last_fetched_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_fetched_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
