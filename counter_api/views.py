from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class CounterView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CounterFilter(APIView):

    def get(self, request, *args, **kwargs):

        start = self.kwargs.get('from')
        end = self.kwargs.get('to')
        # заводим фильтр
        fltr = ['date', 'views', 'clicks', 'cost']
        f = self.kwargs.get('filter')
        if f in fltr:
            counters = Counter.objects.order_by(f).filter(date__gte=start, date__lte=end)
        else:
            counters = Counter.objects.order_by('-date').filter(date__gte=start, date__lte=end)

        serializer = CounterFilterSerializer(counters, many=True)
        return Response({"counters": serializer.data})


def Delete_counters(request):
    try:
        Counter.objects.all().delete()
        print('DELETE ALL RECORDS...')
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")

    return redirect('counters')
