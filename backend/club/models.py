from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=500)
    email=models.EmailField(null=True,blank=True)
    subject=models.CharField(max_length=500,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
    
