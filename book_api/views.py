from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from book_api.models import Book
from .serializers import BookSerializer


class BookView(APIView):
    def get(self, request, pk=None):
        if pk:
            books = Book.objects.get(pk=pk)
            srz_data = BookSerializer(instance=books).data
        else:
            books = Book.objects.all()
            srz_data = BookSerializer(instance=books, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def post(self, request):
        data = BookSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        srz_data = BookSerializer(instance=book, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
