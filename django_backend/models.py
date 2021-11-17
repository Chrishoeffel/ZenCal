from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _



class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:    
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')    
        
        
class Calendar_Event(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    event_date = models.DateField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=120)
    decription = models.CharField(blank=True, max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
