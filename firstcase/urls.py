from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('projects.urls')),
    path('', include('authentication.urls'))
]
