from django.urls import path

from . import views

app_name = 'swapihandler'
urlpatterns = [
    path('', views.index, name='index'),
    path('moviedetail/<int:number>', views.movie_detail, name='moviedetail'),
    path('characterdetail/<int:number>', views.character_detail, name='charaterdetail'),
    ]
