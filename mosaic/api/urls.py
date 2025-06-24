from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from.views import DesignViewSet
router=DefaultRouter()
router.register(r"products",DesignViewSet,basename="product")
urlpatterns=[path("",include(router.urls)),]