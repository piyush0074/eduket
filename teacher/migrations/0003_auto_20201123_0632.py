# Generated by Django 3.1.2 on 2020-11-23 06:32

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='doc_name',
        ),
        migrations.AddField(
            model_name='notes',
            name='uploaded_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='notes',
            name='uploaded_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='doc',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
