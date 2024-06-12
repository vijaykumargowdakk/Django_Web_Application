from django.urls import path
from app2.views import home
urlpatterns = [path('', home),]