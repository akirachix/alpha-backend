
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, OrderViewSet

router = DefaultRouter()
router.register(r"users", UsersViewSet, basename="users")
router.register(r"order", OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]





  

