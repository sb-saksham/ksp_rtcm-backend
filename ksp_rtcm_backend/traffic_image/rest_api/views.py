from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny

from .serializers import TrafficImageSerializer
from traffic_image.models import TrafficImage


class CreateTrafficImage(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]
    queryset = TrafficImage.objects.all()
    serializer_class = TrafficImageSerializer
