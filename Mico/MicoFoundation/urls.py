from django.urls import path, include
from . import views

urlpatterns = [
            path('', views.homepage, name = 'home'),
            path('about/', views.aboutpage, name = 'about'),
            path('boardmembers/', views.boardmembers, name = 'boardmembers'),
            path('sponsorships/', views.sponsorship, name = 'sponsorship'),
            path('contact/', views.contact, name = 'contact'),
            path('donate/', views.donate, name = 'donate'),
            path('getinvolved/', views.getinvolved, name = 'getinvolved'),
            path('history/', views.history, name = 'history'),
            path('ladymessage/', views.ladymessage, name = 'ladymessage'),
            path('managermessage/', views.managermessage, name = 'managermessage'),
            path('messagechairman/', views.messagechairman, name = 'messagechairman'),
            path('newsroom/', views.newsroom, name = 'newsroom'),
            path('covidrelieffund/', views.covidrelief, name = 'covidrelief'),
            path('fenceproject/', views.fenceproject, name = 'fenceproject'),
            path('messages/', views.messages, name = 'messages'),
            path('ourmission/', views.ourmission, name = 'ourmission'),
            path('ressources/', views.resources, name = 'resources'),
            path('smartclassroom/', views.covidrelief, name = 'smartclassroom'),
            path('staffs/', views.staffs, name = 'staffs'),
            path('trustees/', views.trustees, name = 'trustees'),
            path('workwithis/', views.workwithus, name = 'workwithus'),
        
]
