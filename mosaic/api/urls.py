from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from.views import (DesignViewSet,DesignersViewSet,TraderViewSet,OrderViewSet,PaymentViewSet,Shopping_cartViewSet,Transaction,design_review)
router=DefaultRouter()
router.register(r"design",DesignViewSet,basename="design")
router.register(r"designers",DesignViewSet,basename="designers")
router.register(r"trader",DesignViewSet,basename="trader")
router.register(r"order",DesignViewSet,basename="order")
router.register(r"payment",DesignViewSet,basename="payment")
router.register(r"shopping_cart",DesignViewSet,basename="shopping_cart")
router.register(r"transaction",DesignViewSet,basename="transaction")
router.register(r"design_review",DesignViewSet,basename="design_review")


urlpatterns=[path("",include(router.urls)),]