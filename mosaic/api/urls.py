
from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import (Shopping_cartViewSet)

router = DefaultRouter()
router.register(r"shopping_cart", Shopping_cartViewSet, basename="shopping_cart")
urlpatterns = [path("", include(router.urls)),]

