# Generated by Django 3.1.2 on 2020-11-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_account_picture_of_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='picture_of_profile',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
