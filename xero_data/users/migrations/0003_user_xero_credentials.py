# Generated by Django 3.0.7 on 2020-06-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171227_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='xero_credentials',
            field=models.TextField(blank=True, null=True),
        ),
    ]
