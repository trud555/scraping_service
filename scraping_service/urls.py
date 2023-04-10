
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('adminok/', admin.site.urls),
    path('home/', home),
]
