from django.urls import path
# from .. import apps
from .views import getRoom,getRooms,getRoutes
# apps.AppConfig()

urlpatterns = [
    path('',  getRoutes),
    path('rooms/', getRooms),
    path('rooms/<str:pk>/', getRoom),
]
