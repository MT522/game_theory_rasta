from django.db import models

# Create your models here.
class Group(models.Model):
    player1 = models.CharField(max_length=64, blank=True, default='')
    player2 = models.CharField(max_length=64, blank=True, default='')
    player3 = models.CharField(max_length=64, blank=True, default='')
    player4 = models.CharField(max_length=64, blank=True, default='')
    score = models.IntegerField(default=1000)

    def __str__(self):
        return str(self.id) + ' | ' + self.player1 + ' | ' + self.player2 + ' | ' + self.player3 + ' | ' + self.player4
