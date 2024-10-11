from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Collection, Movie
from .serializers import CollectionSerializer, UpdationSerializer, CollectionDeleteSerializer
from django.http import JsonResponse
from django.views import View
from .middleware import RequestCountMiddleware


class CollectionListCreateView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MovieView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        url = "https://demo.credy.in/api/v1/maya/movies/"
        response = requests.get(url, verify=False)

        if response.ok:
            return Response(response.json(), status=status.HTTP_200_OK)
        
        return Response({'error': 'Failed to fetch movies'}, status=status.HTTP_400_BAD_REQUEST)


class CollectionUpdateView(generics.UpdateAPIView):
    serializer_class = UpdationSerializer  # Use the update serializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return generics.get_object_or_404(Collection, uuid=self.kwargs['collection_uuid'], user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)




class CollectionDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Fetch the collection instance based on the UUID
        return generics.get_object_or_404(Collection, uuid=self.kwargs['collection_uuid'], user=self.request.user)

    def delete(self, request, *args, **kwargs):
        collection = self.get_object()
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class RequestCountView(View):
    def get(self, request):
        count = RequestCountMiddleware.request_count
        return JsonResponse({'requests': count})

class RequestCountResetView(View):
    def post(self, request):
        with RequestCountMiddleware.lock:
            RequestCountMiddleware.request_count = 0
        return JsonResponse({'message': 'request count reset successfully'})
