# Generated by Django 3.2.7 on 2024-04-29 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='data_joined',
            new_name='date_joined',
        ),
    ]