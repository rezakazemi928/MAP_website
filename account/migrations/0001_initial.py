# Generated by Django 3.1.2 on 2020-11-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_address', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('voice_file', models.FileField(upload_to='')),
                ('picture_of_profile', models.ImageField(upload_to='')),
                ('picture_of_work', models.ImageField(upload_to='')),
                ('registration_date', models.DateField()),
            ],
        ),
    ]
