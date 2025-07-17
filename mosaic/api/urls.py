
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UsersViewSet, TransactionViewSet, DesignReviewViewSet, DesignViewSet,ShoppingCartViewSet,PaymentViewSet, STKPushView, daraja_callback,OrderViewSet)

router = DefaultRouter()

router.register(r'users', UsersViewSet, basename='users')
router.register(r'transaction', TransactionViewSet, basename='transaction')
router.register(r'design_review', DesignReviewViewSet, basename='design_review')
router.register(r'design', DesignViewSet, basename='design')
router.register(r"shopping_cart", ShoppingCartViewSet, basename="shopping_cart")
router.register(r"payments", PaymentViewSet, basename="payment")
router.register(r'order', OrderViewSet, basename='order')


urlpatterns = [
    path('', include(router.urls)),   
    path("daraja/stk-push/", STKPushView.as_view(), name="daraja-stk-push"),
    path("daraja/callback/", daraja_callback, name="daraja-callback"),
]







