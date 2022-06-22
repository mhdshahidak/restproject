from . import views
from django.urls import path,include
from rest_framework import routers

app_name ='apis'
router = routers.DefaultRouter()
router.register('student', views.Student )
urlpatterns = [
    path('', include(router.urls)),
]