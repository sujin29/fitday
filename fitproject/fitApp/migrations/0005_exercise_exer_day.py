# Generated by Django 3.1.2 on 2020-10-14 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitApp', '0004_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='exer_day',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
