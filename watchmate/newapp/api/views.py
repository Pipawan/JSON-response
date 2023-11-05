from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from newapp.models import Movie
from newapp.api.serializers import MovieSerializer


class MovieListAV(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MovieDetailAV(APIView):
    def get(self, request,pk):
        movies = Movie.objects.filter(pk=pk).first()
        if movies is None:
            return Response({'error':'Movie not found'},status=status.HTTP_204_NO_CONTENT)
        serializer = MovieSerializer(movies)
        return Response(serializer.data)
    

    def put(self, request,pk):
        movies = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)
        

    def delete(self, request,pk):
        movies = Movie.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['GET', 'POST'])
# def Movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def Movie_details(request, pk):

#     if request.method == 'GET':
#         movies = Movie.objects.filter(pk=pk).first()
#         if movies is None:
#             return Response({'error':'Movie not found'},status=status.HTTP_204_NO_CONTENT)
#         serializer = MovieSerializer(movies)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movies = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movies, data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)

#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         movies = Movie.objects.get(pk=pk)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
