# Generated by Django 4.1.7 on 2023-03-17 13:05

from django.db import migrations
import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.managers.CustomUserManager()),
            ],
        ),
    ]