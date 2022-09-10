from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer


@api_view(['GET', 'POST'])
def hello(request):
    # По задумке, в ответ на POST-запрос нужно вернуть JSON с теми данными, 
    # которые получены в запросе.
    # Для этого в объект Response() передаём словарь request.data. 
    if request.method == 'POST':
        return Response({'message': 'Получены данные', 'data': request.data})

    # В ответ на GET-запрос нужно вернуть JSON
    # Он тоже будет создан из словаря, переданного в Response()
    return Response({'message': 'Это был GET-запрос!'})

@api_view(['GET', 'POST'])  # Разрешены только POST- и GET-запросы
def cat_list(request):
    # В случае POST-запроса добавим список записей в БД
    if request.method == 'POST':
        serializer = CatSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # В случае GET-запроса возвращаем список всех котиков
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data) 