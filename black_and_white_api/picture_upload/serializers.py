from atexit import register
from dataclasses import fields
from rest_framework import serializers
from .models import Styles, UploadImage

class StylesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Styles
        fields = ['id', 'style_image', 'style_num']

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ['id', 'contents_image', 'style_num', 'created_image']