# Generated by Django 3.1.2 on 2020-10-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitApp', '0006_auto_20201014_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='nickname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exer_time',
            field=models.IntegerField(),
        ),
    ]
