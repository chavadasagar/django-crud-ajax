# Generated by Django 4.0.3 on 2022-03-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='std',
            name='c_id',
            field=models.IntegerField(default=0),
        ),
    ]