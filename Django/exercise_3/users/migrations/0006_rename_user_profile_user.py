# Generated by Django 4.2.2 on 2023-06-23 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_last_logged'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User',
            new_name='user',
        ),
    ]
