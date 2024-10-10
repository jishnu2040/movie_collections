
from django.urls import path
from .views import CollectionListCreateView, MovieView

urlpatterns = [
    path('collection/', CollectionListCreateView.as_view(), name='collection-list-create'),
    path('movies/', MovieView.as_view(), name='movie-fetch'),
]