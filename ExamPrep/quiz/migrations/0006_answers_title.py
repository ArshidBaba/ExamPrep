# Generated by Django 3.2.9 on 2021-12-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_questions_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
    ]
