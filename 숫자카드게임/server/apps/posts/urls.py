from django.urls import path
from server.apps.posts.views import main

urlpatterns = [
    path("", main),
]