from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (Shopping_cartViewSet, TransactionViewSet, Design_reviewViewSet)

router = DefaultRouter()
router.register(r"shopping_cart", Shopping_cartViewSet, basename="shopping_cart")
router.register(r"transaction", TransactionViewSet, basename="transaction")
router.register(r"design_review", Design_reviewViewSet, basename="design_review")

urlpatterns = [
    path('', include(router.urls)),
]