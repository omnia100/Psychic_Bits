from rest_framework import serializers
from . models import matchData


class matchDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = matchData
        fields = '__all__'