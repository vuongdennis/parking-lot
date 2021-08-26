from rest_framework import serializers
from .models import Space, History

class SpaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Space
        fields = ['id', 'space_number', 'time_in', 'time_out', 'price', 'paid']

class ExitSpaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Space
        fields = ['time_out', 'price', 'paid']

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'space_number', 'time_in', 'time_out', 'price', 'paid']

class ExitHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ['time_out', 'price', 'paid']