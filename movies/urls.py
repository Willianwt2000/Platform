from django.urls import path

from . import views

app_name = "actor"
urlpatterns = [
    path("films", views.movies, name="movies"),
    path("actor", views.actor, name="actor"),
     # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:film_id>/vote/", views.vote, name="vote"),
]
