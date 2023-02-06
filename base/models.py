from django.db import models

# Create your models here.

class Topic(models.Model):
    desc = models.TextField(null=True, blank=True)

class Group(models.Model):
    name = models.CharField(max_length=200)
    #topic = 
    desc = models.TextField(null=True, blank=True)
    #host =
    #participants =
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.id, self.name  