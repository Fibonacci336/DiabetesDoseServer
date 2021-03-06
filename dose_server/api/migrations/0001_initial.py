# Generated by Django 4.0.4 on 2022-05-06 03:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('current_target_bg', models.FloatField(default=0)),
                ('target_bg_duration', models.DurationField(default=datetime.timedelta(seconds=900))),
                ('last_login', models.DateTimeField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='DiabetesEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('blood_glucose', models.FloatField(default=0)),
                ('trend_rate', models.FloatField(default=0, null=True)),
                ('trend', models.TextField(default='none', null=True)),
                ('insulin_on_board', models.FloatField(default=0)),
                ('dosed_insulin', models.FloatField(default=0, null=True)),
                ('dose_completion_time', models.DateTimeField(null=True)),
                ('dose_target_bg', models.FloatField(default=0, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diabetes_entry', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='LoginData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.TextField(max_length=15, unique=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login_data', to='api.user')),
            ],
            options={
                'db_table': 'user_login_data',
            },
        ),
    ]
