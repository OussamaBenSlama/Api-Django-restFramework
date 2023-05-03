from . import views
from django.urls import path 

#create my url 

urlpatterns = [
    path("", views.getRoutes , name="home"),
    path("notes/", views.getNotes, name="notes") ,
    path("notes/<str:pk>/", views.getNote, name="notes") ,
]