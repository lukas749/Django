from django.urls import path
from . import views

urlpatterns = [
    path('domace/', views.domace, name = 'domace'),

]