from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("customers", views.customers, name="customers"),
    # ex: /polls/5/
    path("specifics/<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]