from django.contrib import admin
from server.apps.posts.models import Game, User

# Register your models here.
admin.site.register(User)
admin.site.register(Game)
