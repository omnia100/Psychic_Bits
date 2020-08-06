from rest_framework import serializers
from . models import prediction


class predictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = prediction
        fields = '__all__'