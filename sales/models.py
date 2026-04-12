from django.db import models


# ============================================
# MODELOS FUENTE (PostgreSQL - solo lectura)
# ============================================

class RentalSource(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory_id = models.IntegerField()
    customer_id = models.IntegerField()
    return_date = models.DateTimeField(blank=True, null=True)
    staff_id = models.IntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'rental'
        managed = False


class PaymentSource(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    staff_id = models.IntegerField()
    rental_id = models.IntegerField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    class Meta:
        db_table = 'payment'
        managed = False


# ============================================
# MODELOS DESTINO (SQLite)
# ============================================

class Rental(models.Model):
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(
        'inventory.Inventory',
        on_delete=models.PROTECT,
        db_column='inventory_id'
    )
    customer = models.ForeignKey(
        'users.Customer',
        on_delete=models.PROTECT,
        db_column='customer_id'
    )
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey(
        'users.Staff',
        on_delete=models.PROTECT,
        db_column='staff_id'
    )
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'rental'
        verbose_name = 'Alquiler'
        verbose_name_plural = 'Alquileres'

    def __str__(self):
        return f"Rental {self.id}"


class Payment(models.Model):
    customer = models.ForeignKey(
        'users.Customer',
        on_delete=models.PROTECT,
        db_column='customer_id'
    )
    staff = models.ForeignKey(
        'users.Staff',
        on_delete=models.PROTECT,
        db_column='staff_id'
    )
    rental = models.ForeignKey(
        Rental,
        on_delete=models.PROTECT,
        db_column='rental_id'
    )
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    class Meta:
        db_table = 'payment'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return f"Payment {self.id} - ${self.amount}"
