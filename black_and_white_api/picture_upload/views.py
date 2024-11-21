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
    print(queryset[1].contents_image)
    print(queryset)

    #def perform_create(self, serializer):
        #print("A")
        #print(self.request.data)
        #print(self.request.data.values)
        #print(dir(self.request))
        #print(dir(self.request.data.values))
        #print(dir(serializer.Meta.model.contents_image.field))
        #print(serializer.Meta.model.contents_image)
        #print(self)
        #serializer.save(created_image=self.)
        #print(self.model.created_image)
