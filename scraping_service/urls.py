
from django.contrib import admin
from django.urls import path
from scraping.views import *

urlpatterns = [
    path('adminok/', admin.site.urls),
    path('', home),
]
