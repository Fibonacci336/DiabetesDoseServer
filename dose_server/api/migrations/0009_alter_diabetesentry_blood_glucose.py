# Generated by Django 4.0.4 on 2022-05-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_user_last_fetched_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabetesentry',
            name='blood_glucose',
            field=models.FloatField(default=0, null=True),
        ),
    ]
