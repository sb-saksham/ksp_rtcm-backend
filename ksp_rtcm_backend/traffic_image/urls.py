from django.urls import path, include
from .rest_api.views import CreateTrafficImage

app_name = "traffic_image"

urlpatterns = [
    path('upload/', CreateTrafficImage.as_view(), name="upload_image"),
]
