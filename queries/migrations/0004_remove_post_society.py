# Generated by Django 3.0.3 on 2020-04-21 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0003_auto_20200421_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='society',
        ),
    ]