from django.db import models


# ============================================
# MODELOS FUENTE (PostgreSQL - solo lectura)
# ============================================

class InventorySource(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film_id = models.IntegerField()
    store_id = models.IntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'inventory'
        managed = False


# ============================================
# MODELOS DESTINO (SQLite)
# ============================================

class Inventory(models.Model):
    film = models.ForeignKey(
        'movies.Film',
        on_delete=models.CASCADE,
        db_column='film_id'
    )
    store = models.ForeignKey(
        'stores.Store',
        on_delete=models.CASCADE,
        db_column='store_id'
    )
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'inventory'
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'

    def __str__(self):
        return f"Inventory {self.id} - {self.film}"
