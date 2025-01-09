from django.db import models

# Create your models here.
class Skill(models.Model):
    # name = models.CharField(max_length=250)
    # description = models.TextField()
    skill_level =[
        ('beginner','beginner'),
        ('intermediate','intermediate'),
        ('Professinal','Professinal')
]
    skill = models.CharField(max_length=50, choices=skill_level, default='null')
    
    def __str__(self):
        return f"{self.skill}"
    


class Time_Traveler(models.Model):
    name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    phone = models.SmallIntegerField()
    email = models.EmailField(max_length=200)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, name='Skill')

    def __str__(self):
        return f"{self.name} {self.last_name}"