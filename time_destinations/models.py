from django.db import models

# Create your models here.
class Time_Type(models.Model):
    TYPE_CHOICES = [  
        ('historical', 'historical'),  
        ('futuristic', 'futuristic'),
        ('mythical', 'mythical')
    ]
    type = models.CharField(max_length=250, choices=TYPE_CHOICES, default='null')

    def __str__(self):
        return f"{self.type}"


class Time_Destination(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey('Time_Type', on_delete=models.CASCADE)

    def __str__(self):  
        return f"{self.name}"