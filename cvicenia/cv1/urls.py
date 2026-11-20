from django.urls import path
from . import views

urlpatterns = [
    path("cv1_index/", views.cv1_index, name = "cv1"),
    path("obchod/", views.cv1_obchod, name = "cv1"),
     path("body/", views.cv1_body, name = "c1"),
]
