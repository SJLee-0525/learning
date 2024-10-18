from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/likes/', views.likes, name='likes'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('detail/<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
