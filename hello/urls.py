from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("edson", views.edson, name="edson"),
]
