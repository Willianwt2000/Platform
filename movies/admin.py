from django.contrib import admin
from .models import Film,Language,Category,Actor,FilmActor,FilmCategory
# Register your models here.

admin.site.register(Film)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(FilmActor)
admin.site.register(FilmCategory)
