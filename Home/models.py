from django.db import models

# # Create your models here.
# name phone email message 




class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    message = models.CharField(max_length = 100)
    


    def __str__(self):
        return str(self.name)