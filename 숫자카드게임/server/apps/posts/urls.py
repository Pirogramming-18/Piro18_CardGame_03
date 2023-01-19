from django.urls import path
from server.apps.posts.views import makeCard

urlpatterns = [
    path("gameStatus", makeCard)
]
