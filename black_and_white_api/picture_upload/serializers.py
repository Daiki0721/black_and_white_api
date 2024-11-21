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
#リクエストデータから新しいインスタンスを作成
    def create(self, validated_data):
        print(validated_data)
        print(validated_data['contents_image'])
        created_image = validated_data.get('contents_image', validated_data['contents_image'])
        print(created_image)
        validated_data['created_image'] = created_image
        return UploadImage.objects.create(**validated_data)
