from django_backend.models import Profile, Calendar_Event
from rest_framework import viewsets, permissions
from .serializers import ProfileSerializer, EventSerializer

#Profile Viewsets

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfileSerializer
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Calendar_Event.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    
    serializer_class = EventSerializer
    
