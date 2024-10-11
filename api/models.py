import uuid
from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection')
    title = models.CharField(max_length=125)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=125)
    description = models.TextField()
    genres = models.CharField(max_length=125)

    def __str__(self):
        return self.title
