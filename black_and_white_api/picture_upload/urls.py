from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import StylesViewSet, UploadImageViewSet

router = routers.DefaultRouter()
router.register('styles', StylesViewSet)
router.register('uploadimage', UploadImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

