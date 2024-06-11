from django.urls import path
from app1.views import home
urlpatterns = [path('', home),]