from rest_framework import routers
from .views import *
from django.urls import path,include

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('meals', MealViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
