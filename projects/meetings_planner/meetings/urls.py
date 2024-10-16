from django.urls import path
from . import views

urlpatterns = [
   path('', views.meetings_list_view, name='list'),
   path('room', views.Room_list_view, name='list_Room'),
      path('roomdetail/<int:id>/', views.room, name='room'),


   path('detail/<int:id>/', views.detail, name='detail'),
   path('new', views.add_meeting, name='hhh'), # On passe bien l'ID ici
]
