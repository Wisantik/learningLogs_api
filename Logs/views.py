from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from Logs.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import EntrySerializer, TopicSerializer
from rest_framework.decorators import action
from .models import Topic, Entrys
from rest_framework.permissions import *
from rest_framework.pagination import PageNumberPagination


class EntryListPAGINATION(PageNumberPagination):
    page_size = 3
    # название дополнительного параметра в url для изменения кол страниц
    page_size_query_param = 'page_size'
    max_page_size = 10000  # определяет максимальное кол изменнённого кол страниц


class EntryAPIList(generics.ListCreateAPIView):
    queryset = Entrys.objects.all()
    serializer_class = EntrySerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = EntryListPAGINATION


class EntryAPIUpdate(generics. RetrieveUpdateAPIView):
    queryset = Entrys.objects.all()
    serializer_class = EntrySerializer
    serializer_class = (IsOwnerOrReadOnly,)


class EntryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Entrys.objects.all()
    serializer_class = EntrySerializer
    # permission_classes = (IsAdminOrReadOnly, )


class TopicAPIList(generics. ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicAPIUpdate(generics. UpdateAPIView):
    # берёт не все, а только ту что нужно (ленивый запрос)
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicWithEntry(viewsets.ModelViewSet):
    queryset = Entrys.objects.all()
    serializer_class = EntrySerializer

    @action(methods=['get'], detail=True)
    def topicEntry(self, request, pk):
        entryTopic = Entrys.objects.filter(topic=pk)
        topic_name = Topic.objects.get(pk=pk)
        return Response({topic_name.name: [c.content for c in entryTopic]})
        # для получения всех записей связанных с топиком
