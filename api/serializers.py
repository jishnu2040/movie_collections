from rest_framework import serializers
from .models import Collection, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genres', 'uuid']
        read_only_fields = ['uuid']  # Prevent uuid from being editable


class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Collection
        fields = ['uuid', 'title', 'description', 'movies']  # Removed 'genres'

    def create(self, validated_data):
        movies_data = validated_data.pop('movies')
        collection = Collection.objects.create(**validated_data)

        for movie_data in movies_data:
            Movie.objects.create(collection=collection, **movie_data)

        return collection


class UpdationSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Collection
        fields = ['uuid', 'title', 'description', 'movies']

    def update(self, instance, validated_data):
        movies_data = validated_data.pop('movies', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Update or create movie instances
        for movie_data in movies_data:
            movie_uuid = movie_data.get('uuid')
            if movie_uuid:
                movie = Movie.objects.filter(uuid=movie_uuid, collection=instance).first()
                if movie:
                    for attr, value in movie_data.items():
                        setattr(movie, attr, value)
                    movie.save()
                else:
                    Movie.objects.create(collection=instance, **movie_data)
            else:
                Movie.objects.create(collection=instance, **movie_data)

        return instance


class CollectionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['uuid']

    def validate_uuid(self, value):
        # Optional: Validate if the collection exists
        if not Collection.objects.filter(uuid=value).exists():
            raise serializers.ValidationError("Collection does not exist.")
        return value