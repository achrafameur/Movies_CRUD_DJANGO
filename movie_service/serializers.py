from rest_framework import serializers
from .models import Movie, Category, Cinema, Room, Reservation, Seance

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['uid', 'name','description', 'rate','duration', 'hasReservationsAvailable', 'createdAt', 'updatedAt']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['uid', 'name', 'createdAt']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['uid', 'name', 'seats']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['uid', 'rank', 'status', 'seats', 'createdAt', 'updatedAt', 'expiresAt']

class SeanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seance
        fields = ['uid', 'movie', 'date']