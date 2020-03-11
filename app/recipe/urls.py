from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipe'  # for reverse lookup purpose

urlpatterns = [
    path('', include(router.urls))
]
