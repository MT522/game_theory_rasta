from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('theory/', views.theory_view, name='theory'),
    path('addscore/', views.addScore_view, name='addscore'),
    path('standings/', views.standings_view, name='standings'),
    path('number/', views.number_view, name='number'),
    path('plot/', views.plot_group_data, name='plot')
]
