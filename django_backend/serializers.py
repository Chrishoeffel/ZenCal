from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Profile, Calendar_Event


class ProfileSerializer(ModelSerializer):
    class Meta:
        model: Profile
        fields: "__all__"
 
class EventSerializer(ModelSerializer):
    class Meta:
        model: Calendar_Event
        fields: "__all__"