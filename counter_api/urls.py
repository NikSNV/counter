from django.conf.urls import url
from django.urls import path

from .views import *


# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('counters/', CounterView.as_view(), name='counters'),
    url(r'^counters/(?P<from>[\w\-\.]+)/(?P<to>[\w\-\.]+)/(?P<filter>[\w]+)/$', CounterFilter.as_view()),
    # url(r'^counters/(?P<from>[\w\-\.]+)/(?P<to>[\w\-\.]*[\w])/$', CounterFilter.as_view()),

    url(r'^counters/(?P<from>[\w\-\.]+)/(?P<to>[\w\-\.]+)/$', CounterFilter.as_view()),
    path('delete/', Delete_counters),

]