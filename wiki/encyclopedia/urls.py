from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("find", views.find, name="find"),
    path("add", views.add, name="add"),
    path("edit/<str:entry_name>", views.edit, name="edit"),
    path("random", views.r_article, name="random"),
    path("<str:entry_name>", views.article, name="article"),
]
