# Generated by Django 3.1.2 on 2020-10-14 13:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitApp', '0005_exercise_exer_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='exer_day',
        ),
        migrations.AddField(
            model_name='exercise',
            name='exer_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='today',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
