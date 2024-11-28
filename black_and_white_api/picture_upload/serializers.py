from atexit import register
from dataclasses import fields
from rest_framework import serializers
from .models import Styles, UploadImage

from PIL import Image, ImageFilter
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

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
        #postされたvalidated_dataを表示
        print(validated_data)
        #contents_imageをopen
        contents_image = validated_data.get('contents_image', validated_data['contents_image'])
        org_img = Image.open(contents_image)
        #白黒変換
        created_image = org_img.convert('L')
        print(created_image)
        #BytesIOとは、メモリ上でバイナリデータを扱うための機能です。Python の標準ライブラリ io に含まれています。
        image_io = io.BytesIO()
        #io.BytesIO に保存！ Pillow.Image.save は第一引数に seek や tell や write を持っているオブジェクトが必要io.BytesIO は問題なさそう　
        created_image.save(image_io, format="JPEG")
        #InMemoryUploadedFileに変換
        created_image = InMemoryUploadedFile(image_io, field_name=None, name="grayscale.jpg", content_type="image/jpeg", size=image_io.getbuffer().nbytes, charset=None)
        #validated_data(辞書型)にcreated_imageを追加
        validated_data['created_image'] = created_image
        print(validated_data)
        # 以前保存した画像処理後の画像ファイルを削除
        UploadImage.delete(UploadImage)
        #model(UploadImage)にvalidated_dataを保存
        return UploadImage.objects.create(**validated_data)
