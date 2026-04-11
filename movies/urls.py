from django.urls import path

from . import views

urlpatterns = [
    path("films", views.movies, name="movies"),
]