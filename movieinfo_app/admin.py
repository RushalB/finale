from django.contrib import admin

# Register your models here.
from movieinfo_app.models import Director, Actor, Movie, Platform, Casting, Watching, Genre

admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Platform)
admin.site.register(Casting)
admin.site.register(Watching)
admin.site.register(Genre)
