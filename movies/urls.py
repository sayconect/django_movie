from os import name
from .views import *
from django.urls import path

urlpatterns = [
    path('', MovieList.as_view(), name='home'),
    path('filter/', MovieListByFilter.as_view(), name='filter'),
    path('search/', MoviesBySearch.as_view(), name='search'),
    path('review/<int:pk>',AddReview.as_view(), name='review'),
    path('category/<slug:categ_slug>', MovieListByCategory.as_view(), name='category'),
    path('actor/<str:slug>', ActorInfo.as_view(), name='actor'),
    path('<slug:slug>/', SingleMovie.as_view(), name='movie'),



]