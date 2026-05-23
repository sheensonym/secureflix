from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'movie/<int:pk>/',
        views.movie_detail,
        name='movie_detail'
    ),

    path(
        'upload/',
        views.upload_movie,
        name='upload_movie'
    ),

    path(
        'edit/<int:pk>/',
        views.edit_movie,
        name='edit_movie'
    ),

    path(
        'delete/<int:pk>/',
        views.delete_movie,
        name='delete_movie'
    ),

    path(
       'dashboard/',
        views.admin_dashboard,
        name='dashboard'
    ),

    path(
    'delete-user/<int:pk>/',
    views.delete_user,
    name='delete_user'
),
]