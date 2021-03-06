from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Musics
from .serializers import MusicsSerializer
from .pagination import CustomPagination
class MusicsView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    pagination_class = CustomPagination

    def get(self, request):
        music = Musics.objects.all()
        serializer = MusicsSerializer(music, many=True)
        return Response({"music": serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = MusicsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MusicsDetail(APIView):
    def get_object(self, pk):
        try:
            return Musics.objects.get(pk=pk)
        except Musics.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicsSerializer(music)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicsSerializer(music, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        music = self.get_object(pk)
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
