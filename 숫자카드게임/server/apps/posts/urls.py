from django.urls import path
from server.apps.posts.views import makeCard, makeCard2, userCreate, GameCreate, counterattack, gameStart

urlpatterns = [
  path("", userCreate),
  path("gameStatus/<int:pk>", gameStart),
  path("attack/<str:uid>",  GameCreate, name="attack"),
  # path("attack/<str:uid>", cardCreate),
  path("counterattack/<int:pk>", counterattack, name="counterattack"),
]