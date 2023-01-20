from django.contrib import admin
from .models import User,GestUser,Game

admin.site.register(Game)
admin.site.register(User)
admin.site.register(GestUser)
