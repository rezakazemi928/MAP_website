# Generated by Django 3.1.2 on 2020-11-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20201123_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email_address',
            field=models.CharField(max_length=250, null=True, unique=True),
        ),
    ]
