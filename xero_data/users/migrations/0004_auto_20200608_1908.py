# Generated by Django 3.0.7 on 2020-06-08 19:08

from django.contrib.auth import get_user_model
from django.db import migrations


def forwards_func(apps, schema_editor):
    # build the user we now have access to via Django magic
    User = get_user_model()
    is_username_exist = User.objects.filter(username="admin").exists()
    if not is_username_exist:
        User.objects.create_superuser(
            username="admin", email="admin@admin.com", password="adminpassword",
        )


def reverse_func(apps, schema_editor):
    # destroy what forward_func build
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_xero_credentials'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func,),
    ]
