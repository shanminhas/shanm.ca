# Generated by Django 3.0.2 on 2020-02-04 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techmed', '0005_auto_20200203_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='slug',
        ),
    ]
