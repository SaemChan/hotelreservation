# Generated by Django 2.2.5 on 2020-09-28 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_login_method'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='superhost',
            new_name='tophost',
        ),
    ]