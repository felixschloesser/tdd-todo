from django.urls import path

from lists import views

urlpatterns = [
    path("", views.home, name="home"),
    path("lists/new", views.new_list, name="new_list"),
    path("lists/the-only-list-in-the-world/", views.list, name="list_view"),
]
