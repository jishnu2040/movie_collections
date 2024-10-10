from rest_framework import serializers
from .models import Collection, Movie





class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genres', 'uuid']



class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True) 

    class Meta:
        model = Collection
        fields = ['id', 'title', 'description', 'movies']

    def create(self, validated_data):
        # Pop the movies data from validated_data
        movies_data = validated_data.pop('movies')  

        # Create the collection instance without the user field
        collection = Collection.objects.create(**validated_data)  
        
        # Create Movie instances and link them to the collection
        for movie_data in movies_data:
            Movie.objects.create(collection=collection, **movie_data)  

        return collection
