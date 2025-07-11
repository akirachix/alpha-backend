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

from .views import OrderViewSet

router = DefaultRouter()
router.register(r"order", OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]


