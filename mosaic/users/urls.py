<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet


router = DefaultRouter()
router.register(r'users', UsersViewSet)


urlpatterns = [
   path('', include(router.urls)),
]
=======
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user-create'),
]




>>>>>>> af3f64c53f9e112c757ad6cc5ba6edcbfb6c27e8
