from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Edu_module, Section
from .serializers import *

# Для разнообразия виды для модели Edu_modules я реализовал на более низком уровне,
# а виды модели Section на высоком уровне. Тоже самое я сделал и с сериализаторами
# этих моделей

class Edu_ModuleList(APIView):
    #получаем список всех модулей
    def get(self, request):
        modules = Edu_module.objects.all()
        serializer = Edu_ModuleSerializer(modules, many=True)
        return Response({'modules': serializer.data})

    #добавляем в список новый модуль
    def post(self, request):
        serializer = Edu_ModuleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'modules': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Edu_ModuleDetail(APIView):
    def get_object(self, pk):
        try:
            return Edu_module.objects.get(pk=pk)
        except Edu_module.DoesNotExist:
            raise Http404

    #получаем конкретный модуль по его id
    def get(self, request, pk):
        module = self.get_object(pk)
        serializer = Edu_ModuleSerializer(module)
        return Response({'module': serializer.data})

    #изменяем данные конкретного модуля по его id
    def put(self, request, pk):
        module = self.get_object(pk)
        serializer = Edu_ModuleSerializer(module, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'module': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #удаляем конкретный модуль по его id
    def delete(self, request, pk):
        module = self.get_object(pk)
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


