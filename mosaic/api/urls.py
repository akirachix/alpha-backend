

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
]





from .views import ( TransactionViewSet, DesignReviewViewSet)
router = DefaultRouter()
router.register(r"transaction", TransactionViewSet, basename="transaction")
router.register(r"design_review", DesignReviewViewSet, basename="design_review")
urlpatterns = [
   path('', include(router.urls)),
]

from django.urls import path ,include
from rest_framework.routers import DefaultRouter

from .views import ShoppingCartViewSet

from .views import PaymentViewSet, STKPushView, daraja_callback



router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payment")

urlpatterns = [
    path("", include(router.urls)),
    path("daraja/stk-push/", STKPushView.as_view(), name="daraja-stk-push"),
    path("daraja/callback/", daraja_callback, name="daraja-callback"),
]



router = DefaultRouter()
router.register(r"shopping_cart", ShoppingCartViewSet, basename="shopping_cart")
urlpatterns = [path("", include(router.urls)),]