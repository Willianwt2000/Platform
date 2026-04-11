from django.db import models

class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField()
    language_id = models.IntegerField()
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.IntegerField()
    replacement_cost = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.CharField(max_length=10)
    last_update = models.DateTimeField(auto_now=True)
    special_features = models.JSONField(blank=True, null=True)
    fulltext = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title