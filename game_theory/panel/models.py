from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Group(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    

    player1 = models.CharField(max_length=64, blank=True, default='')
    player2 = models.CharField(max_length=64, blank=True, default='')
    player3 = models.CharField(max_length=64, blank=True, default='')
    player4 = models.CharField(max_length=64, blank=True, default='')
    score = models.IntegerField(default=1000)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')
    number1 = models.FloatField(null=True, blank=True)
    number2 = models.FloatField(null=True, blank=True)
    number3 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' | ' + self.player1 + ' | ' + self.player2 + ' | ' + self.player3 + ' | ' + self.player4
