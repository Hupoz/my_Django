# Generated by Django 3.0.7 on 2020-06-22 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CardManage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publish',
        ),
    ]
