# Generated by Django 3.2.9 on 2021-11-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar_event',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
