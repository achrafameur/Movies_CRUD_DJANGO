from rest_framework import serializers
from .models import Movie, Category

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name','description', 'rate','duration', 'hasReservationsAvailable', 'createdAt', 'updatedAt']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']