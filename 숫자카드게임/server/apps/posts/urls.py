from django.urls import path
from server.apps.posts.views import makeCard, userCreate #, cardCreate

urlpatterns = [
  path("", userCreate),
  path("gameStatus", makeCard),
  path("attack/<str:uid>", makeCard, name="attack"),
  # path("attack/<str:uid>", cardCreate),
  path("counterattack", makeCard, name="counterattack"),
]