from django.urls import path
from factorial.views import home
urlpatterns = [path('', home),]