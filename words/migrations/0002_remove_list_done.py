# Generated by Django 3.0.1 on 2019-12-22 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='done',
        ),
    ]