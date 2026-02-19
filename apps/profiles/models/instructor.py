from django.db import models
from django.conf import settings

class Instructor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.URLfield(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    social_networks = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Instructor: {self.user.get_full_name() or self.user.username}"