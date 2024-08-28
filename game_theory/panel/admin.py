from django.contrib import admin
from .models import Group

# Register your models here.

# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    search_fields = ['player1', 'player2', 'player3', 'player4', 'score', 'gender']

admin.site.register(Group, GroupAdmin)
