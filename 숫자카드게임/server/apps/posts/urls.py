from django.urls import path
from server.apps.posts.views import makeCard, userCreate, GameCreate

urlpatterns = [
  path("", userCreate),
  path("gameStatus", makeCard),
  path("attack/<str:uid>", makeCard, name="attack"),
  path("attack/<str:uid>", GameCreate, name="makeGame"),
  
  # path("attack/<str:uid>", cardCreate),
  path("counterattack", makeCard, name="counterattack"),
]