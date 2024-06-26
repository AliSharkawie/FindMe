# Generated by Django 5.0.4 on 2024-04-22 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0002_alter_lostperson_options_lostperson_photo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lostperson',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='lostperson',
            name='current_date_time',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AddField(
            model_name='lostperson',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='lostperson',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='lostperson',
            name='age',
            field=models.FloatField(default=10),
        ),
    ]
