from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CidadeViewSet

router = DefaultRouter()
router.register(r'cidades', CidadeViewSet, basename='cidade')

urlpatterns = [
    path('', include(router.urls)),
]