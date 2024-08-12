from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('addscore/', views.addScore_view, name='addscore'),
    path('standings/', views.standings_view, name='standings')
]
