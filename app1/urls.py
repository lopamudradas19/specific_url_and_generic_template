from app1.views import *
from django.urls import path
app_name='app1'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('virat2/',virat2,name='virat2'),
]