# Generated by Django 3.1.3 on 2021-02-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_emailtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='pygymuser',
            name='additional_quiz_time_absolute',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pygymuser',
            name='additional_quiz_time_percent',
            field=models.FloatField(default=0),
        ),
    ]
