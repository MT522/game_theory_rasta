from django.db import models
from django.contrib.auth.models import User
from panel.models import Group

# Create your models here.
class GTUser(User):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
