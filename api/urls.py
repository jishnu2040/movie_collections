
from django.urls import path
from .views import CollectionListCreateView, MovieView, CollectionUpdateView, CollectionDeleteView, RequestCountView, RequestCountResetView

urlpatterns = [
    path('collection/', CollectionListCreateView.as_view(), name='collection-list-create'),
    path('movies/', MovieView.as_view(), name='movie-fetch'),
    path('collection/<uuid:collection_uuid>/', CollectionUpdateView.as_view(), name='collection-update'),
    path('collection/<uuid:collection_uuid>/delete/', CollectionDeleteView.as_view(), name='collection-delete'), 
    path('request-count/', RequestCountView.as_view(), name='request-count'),
    path('request-count/reset/', RequestCountResetView.as_view(), name='request-count-reset'),
]