from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StylesSerializer, UploadImageSerializer
from .models import Styles, UploadImage

# Create your views here.
class StylesViewSet(viewsets.ModelViewSet):
    queryset = Styles.objects.all()
    serializer_class = StylesSerializer

class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer
    model = UploadImage
