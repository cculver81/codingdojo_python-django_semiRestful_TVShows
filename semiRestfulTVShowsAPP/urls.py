from django.urls import path
from semiRestfulTVShowsAPP import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.newShow),
    path('shows/create', views.createShow),
    path('shows/<int:showID>/edit', views.editShow),
    path('shows/<int:showID>/update', views.updateShow),
    path('shows/<int:showID>', views.tvShow),
    path('shows/<int:showID>/destroy', views.deleteShow)
]