from django.urls import path, include
from . import views

urlpatterns = [
            path('', views.homepage, name = 'home'),
            path('about/', views.aboutpage, name = 'about'),
            path('boardmembers/', views.boardmembers, name = 'boardmembers'),


]
