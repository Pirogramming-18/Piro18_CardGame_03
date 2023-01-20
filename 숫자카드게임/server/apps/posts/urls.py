from django.urls import path
from server.apps.posts.views import makeCard

urlpatterns = [
    path("attack", makeCard, name="attack"),
    path("counterattack", makeCard, name="counterattack"),
]