# Generated by Django 4.2.2 on 2023-06-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_last_failed_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_failed_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_logged',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
