# Generated by Django 3.0.3 on 2020-04-21 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('queries', '0002_post_society'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='society',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Society'),
        ),
    ]