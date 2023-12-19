from django.db import models
class Contact(models.Model):
    name= models.CharField(max_length=100)
    subject=models.TextField()
    email= models.CharField(max_length=100)
    desc=models.TextField()
    date= models.DateField()
# Create your models here.
    def __str__(self):
        return self.name

#make migrations --- creates changes and saves them 

# migrate --- appliies the pending changes by make migrations 
