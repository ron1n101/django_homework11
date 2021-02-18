from . import views
from django.urls import path

urlpatterns = [
    path('', views.tag, name='tag'),
]