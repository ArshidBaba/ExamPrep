# Generated by Django 3.2.9 on 2021-12-08 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20211208_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='title',
        ),
    ]