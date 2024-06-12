from rest_framework import generics
from .models import Movie, Category, Cinema, Room, Reservation, Seance
from .serializers import MovieSerializer, CategorySerializer, RoomSerializer, ReservationSerializer, CinemaSerializer, SeanceSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta

class MovieList(APIView):
    def get(self, request):
        try:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class MovieDetail(APIView):
    def get(self, request, uid):
        try:
            movie = get_object_or_404(Movie, uid=uid)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, uid):
        try:
            movie = get_object_or_404(Movie, uid=uid)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, uid):
        try:
            movie = get_object_or_404(Movie, uid=uid)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MovieCategories(APIView):
    def get(self, request, uid):
        try:
            movie = get_object_or_404(Movie, uid=uid)
            categories = movie.categories.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoryMovies(APIView):
    def get(self, request, uid):
        try:
            category = get_object_or_404(Category, uid=uid)
            movies = category.movie_set.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MovieSearch(APIView):
    def post(self, request):
        # Récupérer les critères de recherche du corps de la requête POST
        search_criteria = request.data
        # Filtrer les films en fonction des critères de recherche
        queryset = Movie.objects.all()
        if 'name' in search_criteria:
            queryset = queryset.filter(name__icontains=search_criteria['name'])
        if 'description' in search_criteria:
            queryset = queryset.filter(description__icontains=search_criteria['description'])
        # Serializer les films trouvés
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryCreate(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CinemaListCreate(APIView):
    def get(self, request):
        cinemas = Cinema.objects.all()
        serializer = CinemaSerializer(cinemas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CinemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CinemaDetail(APIView):
    def get(self, request, uid):
        try:
            cinema = Cinema.objects.get(uid=uid)
            serializer = CinemaSerializer(cinema)
            return Response(serializer.data)
        except Cinema.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, uid):
        try:
            cinema = Cinema.objects.get(uid=uid)
            serializer = CinemaSerializer(cinema, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Cinema.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, uid):
        try:
            cinema = Cinema.objects.get(uid=uid)
            cinema.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cinema.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

class RoomListCreate(APIView):
    def get(self, request, cinemaUid):
        try:
            cinema = Cinema.objects.get(uid=cinemaUid)
            rooms = cinema.rooms.all()
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data)
        except Cinema.DoesNotExist:
            return Response({"detail": "Cinema not found."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, cinemaUid):
        try:
            cinema = Cinema.objects.get(uid=cinemaUid)
            serializer = RoomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(cinema=cinema)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Cinema.DoesNotExist:
            return Response({"detail": "Cinema not found."}, status=status.HTTP_404_NOT_FOUND)

class RoomDetail(APIView):
    def get(self, request, cinemaUid, uid):
        try:
            room = Room.objects.get(uid=uid, cinema__uid=cinemaUid)
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        except Room.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, cinemaUid, uid):
        try:
            room = Room.objects.get(uid=uid, cinema__uid=cinemaUid)
            serializer = RoomSerializer(room, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Room.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, cinemaUid, uid):
        try:
            room = Room.objects.get(uid=uid, cinema__uid=cinemaUid)
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Room.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

class SeanceListCreate(APIView):
    def get(self, request, cinemaUid, roomUid):
        try:
            room = Room.objects.get(uid=roomUid, cinema__uid=cinemaUid)
            seances = room.seances.all()
            serializer = SeanceSerializer(seances, many=True)
            return Response(serializer.data)
        except Room.DoesNotExist:
            return Response({"detail": "Room not found."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, cinemaUid, roomUid):
        try:
            room = Room.objects.get(uid=roomUid, cinema__uid=cinemaUid)
            serializer = SeanceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(room=room)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Room.DoesNotExist:
            return Response({"detail": "Room not found."}, status=status.HTTP_404_NOT_FOUND)

class SeanceDetail(APIView):
    def put(self, request, cinemaUid, roomUid, uid):
        try:
            seance = Seance.objects.get(uid=uid, room__uid=roomUid, room__cinema__uid=cinemaUid)
            serializer = SeanceSerializer(seance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Seance.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, cinemaUid, roomUid, uid):
        try:
            seance = Seance.objects.get(uid=uid, room__uid=roomUid, room__cinema__uid=cinemaUid)
            seance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Seance.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

class ReservationListCreate(APIView):
    def get(self, request, movieUid):
        reservations = Reservation.objects.filter(seance__movie=movieUid)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request, movieUid):
        seance_uid = request.data.get('seance')
        seats = request.data.get('seats')
        try:
            seance = Seance.objects.get(uid=seance_uid, movie=movieUid)
            reservation = Reservation.objects.create(
                seance=seance,
                seats=seats,
                status='open',
                rank=Reservation.objects.filter(seance=seance).count() + 1,
                expiresAt=timezone.now() + timedelta(hours=1)
            )
            serializer = ReservationSerializer(reservation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Seance.DoesNotExist:
            return Response({"detail": "Seance not found."}, status=status.HTTP_404_NOT_FOUND)

class ReservationConfirm(APIView):
    def post(self, request, uid):
        try:
            reservation = Reservation.objects.get(uid=uid)
            if reservation.status == 'open':
                reservation.status = 'confirmed'
                reservation.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Reservation cannot be confirmed."}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Reservation.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

class ReservationDetail(APIView):
    def get(self, request, uid):
        try:
            reservation = Reservation.objects.get(uid=uid)
            serializer = ReservationSerializer(reservation)
            return Response(serializer.data)
        except Reservation.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

