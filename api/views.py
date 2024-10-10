
import os
import requests
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Collection
from .serializers import CollectionSerializer


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
        response = requests.get(url,verify=False)

        if response.ok:
            return Response(response.json(), status=status.HTTP_200_OK)
        
        return Response({'error':'Failed to fetch movies'}, status=status.HTTP_400_BAD_REQUEST)