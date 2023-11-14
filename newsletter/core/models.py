from django.db import models
from ckeditor.fields import RichTextField

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    

class EmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    message = RichTextField()
    recipients = models.ManyToManyField(Subscriber)
   

    def __str__(self):
        return self.subject