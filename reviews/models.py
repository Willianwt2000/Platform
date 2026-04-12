from django.db import models


# ============================================
# MODELOS FUENTE (PostgreSQL - solo lectura)
# ============================================

class ReviewSource(models.Model):
    review_id = models.AutoField(primary_key=True)
    film_id = models.IntegerField()
    customer_id = models.IntegerField()
    rating = models.IntegerField()
    review_text = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField()

    class Meta:
        db_table = 'review'
        managed = False


# ============================================
# MODELOS DESTINO (SQLite)
# ============================================

class Review(models.Model):
    film = models.ForeignKey(
        'movies.Film',
        on_delete=models.CASCADE,
        db_column='film_id'
    )
    customer = models.ForeignKey(
        'users.Customer',
        on_delete=models.CASCADE,
        db_column='customer_id'
    )
    rating = models.IntegerField()
    review_text = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField()

    class Meta:
        db_table = 'review'
        verbose_name = 'Resena'
        verbose_name_plural = 'Resenas'

    def __str__(self):
        return f"Review {self.id} - Rating {self.rating}"
