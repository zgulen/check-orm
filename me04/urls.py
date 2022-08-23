from django.urls import path
from me04.views import me04

urlpatterns = [
    path("", me04)
]
