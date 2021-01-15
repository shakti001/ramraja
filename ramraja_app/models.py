from django.db import models

# Create your models here.
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    profile = models.CharField(max_length = 50)

    image = models.ImageField()

    def __str__(self):
        return self.name

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    logo = models.ImageField()
    head = models.CharField(max_length = 50)
    discripation = models.CharField(max_length = 255)

   

    def __str__(self):
        return self.head

class Contact(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length =50,blank=True, null=True)
   email = models.EmailField()
   subject = models.CharField(max_length =255 )

   message = models.CharField(max_length =255 )
   def __str__(self):
        return self.name

