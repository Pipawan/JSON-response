from django.urls import path, include
from newapp.api.views import MovieListAV, MovieDetailAV
# from newapp.api.views import Movie_list, Movie_details
urlpatterns = [
    path('list/',MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>',MovieDetailAV.as_view(),name='movie-detail'),

]
