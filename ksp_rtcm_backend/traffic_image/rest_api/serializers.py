from rest_framework import serializers

from traffic_image.models import TrafficImage


class TrafficImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = TrafficImage
        fields = ['junction', 'direction', 'image']
