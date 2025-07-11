<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
]




=======
from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from.views import DesignViewSet
router=DefaultRouter()
router.register(r"design",DesignViewSet,basename="design")
urlpatterns=[path("",include(router.urls)),]
>>>>>>> f716beba9e48da903ad17573b6fdc841dc4e42ad



