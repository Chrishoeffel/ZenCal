from django.db import models

class Snippet(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    event_date = models.DateField(auto_now_add=True, default="Event Date")
    location = models.CharField(max_length=120)
    decription = models.CharField(blank=True, max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
