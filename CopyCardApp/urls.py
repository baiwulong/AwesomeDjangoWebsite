from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name='CopyCardApp.add'),
    path('remove', views.remove, name="CopyCardApp.remove"),
    path('list', views.list, name="CopyCardApp.list"),
]
