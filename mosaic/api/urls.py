<<<<<<< HEAD

=======
>>>>>>> df0fd973e8168909e79b74a49ccc5e5df48df02a
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
]




<<<<<<< HEAD

from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from.views import DesignViewSet
router=DefaultRouter()
router.register(r"design",DesignViewSet,basename="design")
urlpatterns=[path("",include(router.urls)),]

=======
>>>>>>> df0fd973e8168909e79b74a49ccc5e5df48df02a

from .views import ( TransactionViewSet, DesignReviewViewSet)
router = DefaultRouter()
router.register(r"transaction", TransactionViewSet, basename="transaction")
router.register(r"design_review", DesignReviewViewSet, basename="design_review")
urlpatterns = [
   path('', include(router.urls)),
]
from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from.views import DesignViewSet
router=DefaultRouter()
router.register(r"design",DesignViewSet,basename="design")
urlpatterns=[path("",include(router.urls)),]


