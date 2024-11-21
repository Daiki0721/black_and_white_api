from django.db import models
import os
from django.core.exceptions import ValidationError
import io
from PIL import Image
from django.conf import settings


def validate_is_picture(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in ['.jpg', '.png', '.jpeg']:
        raise ValidationError('Only picure files are availables.')

MAX_SIZE    = 1 * 1000 * 1000

def validate_max_size(value):
    if value.size > MAX_SIZE:
        print('ファイルサイズが上限' + str(MAX_SIZE/1000000) + 'MBを超えています。送信されたファイルサイズ: ' + str(value.size/1000000) + "MB")
        raise ValidationError( "ファイルサイズが上限(" + str(MAX_SIZE/1000000) + "MB)を超えています。送信されたファイルサイズ: " + str(value.size/1000000) + "MB")

    else:
        print("問題なし")


class Styles(models.Model):
    id = models.AutoField(primary_key=True)
    style_image = models.ImageField(verbose_name='style_image',upload_to='styles_img/',)
    style_num = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Styles'


class UploadImage(models.Model):
    id = models.AutoField(primary_key=True)
    contents_image = models.ImageField(verbose_name='contents_image', upload_to='img/', validators=[validate_is_picture, validate_max_size],)
    style_num = models.ForeignKey(Styles, on_delete=models.CASCADE)
    created_image = models.ImageField(verbose_name='created_image', upload_to='created_img/',null=True)

    class Meta:
        verbose_name_plural = 'UploadImage'

    def transform(self):

        # アップロードされたファイルから画像オブジェクト生成
        org_img = Image.open(self.contents_image)

        # PILでの画像処理ここから！
        gray_img = org_img.convert('L')

        # PILでの画像処理ここまで！

        # 画像処理後の画像のデータをbufferに保存
        buffer = io.BytesIO()
        gray_img.save(fp=buffer, format=org_img.format)

        # 以前保存した画像処理後の画像ファイルを削除
        self.created_image.delete()

        # bufferのデータをファイルとして保存（レコードの更新も行われる）
        self.save(name=self.name, content=buffer)
