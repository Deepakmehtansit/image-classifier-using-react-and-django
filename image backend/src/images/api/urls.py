from .views import ImageViewSet, index
from rest_framework import routers
from django.urls import path, include
# from .views import index
app_name = 'api-images'

router = routers.DefaultRouter()
router.register(r'images',ImageViewSet)

urlpatterns = [
    path('index', index, name='index'),
    path('', include(router.urls))

]