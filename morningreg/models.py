from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name