# Generated by Django 3.1.6 on 2021-02-18 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField('Article', 'auth', 'author'),
    ]
