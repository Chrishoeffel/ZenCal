from django.urls import path
from . import views
from rest_framework import routers
from .api import ProfileViewSet, EventViewSet

#router = routers.DefaultRouter()
#router.register('api.django_backend', ProfileViewSet, "profiles")
#router.register('api.django_backend', EventViewSet, "Calendar_Events")
urlpatterns = [
    path('', views.getRoutes, name='home'),
    path('events/', views.getEvents, name="events"),
    path('events/<str:pk>', views.getEvent, name="event"),
]