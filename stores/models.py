from django.db import models

# Create your models here.    
class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.country
