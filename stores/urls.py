from django.urls import path

from . import views

urlpatterns = [
    path("country", views.stores, name="stores"),
]
