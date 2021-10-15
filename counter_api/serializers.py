from rest_framework import serializers
from .models import *


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ('date', 'views', 'clicks', 'cost')


class CounterFilterSerializer(serializers.ModelSerializer):
    cpc = serializers.SerializerMethodField()  # add field
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = Counter
        fields = ('date', 'views', 'clicks', 'cost', 'cpc', 'cpm')

    def get_cpc(self, obj):
        # here write the logic to compute the value based on object
        # Округляем до копеек
        cpc_tmp = round(obj.cost / obj.clicks, 2)
        return cpc_tmp

    def get_cpm(self, obj):
        # here write the logic to compute the value based on object
        cpm_tmp = round(obj.cost / obj.views, 2)
        return cpm_tmp