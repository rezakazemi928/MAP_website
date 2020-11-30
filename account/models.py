from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length = 200 , null = True)
    last_name = models.CharField(max_length = 200 , null = True)
    email_address = models.CharField(max_length = 250 , null = True , unique = True , error_messages = {'unique' : 'This email address hasbeen already taken'})
    password = models.CharField(max_length = 250 , null = True)
    username = models.CharField(max_length = 150 , null = True , unique = True , error_messages = {'unique' : 'This username has already been taken'})
    picture_of_profile = models.ImageField(null = True)
    registration_date = models.DateField(null = True)

    def __str__(self):
        return self.username


class VoiceFile(models.Model):
    file_name = models.CharField(max_length = 250 , null = True)
    voice_file = models.FileField()
    creation_date = models.DateTimeField(null = True)
    file_picture = models.ImageField()
    description = models.TextField(null = True)
    file_username = models.ForeignKey(Account , null = True , on_delete = models.SET_NULL)

