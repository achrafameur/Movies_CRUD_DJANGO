from rest_framework import generics
from .models import Movie, Category
from .serializers import MovieSerializer, CategorySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class MovieListCreate(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if description:
            queryset = queryset.filter(description__icontains=description)
        return queryset

class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCategories(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        categories = instance.categories.all()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)

class CategoryMovies(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        movies = instance.movie_set.all()
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)

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

