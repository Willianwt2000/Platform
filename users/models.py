from django.db import models


# ============================================
# MODELOS FUENTE (PostgreSQL - solo lectura)
# ============================================

class CustomerSource(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=50, null=True, blank=True)
    address_id = models.IntegerField()
    activebool = models.BooleanField()
    create_date = models.DateField()
    last_update = models.DateTimeField()
    active = models.IntegerField()

    class Meta:
        db_table = 'customer'
        managed = False


class StaffSource(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address_id = models.IntegerField()
    email = models.EmailField(max_length=50, null=True, blank=True)
    store_id = models.IntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    picture = models.BinaryField(null=True, blank=True)

    class Meta:
        db_table = 'staff'
        managed = False


# ============================================
# MODELOS DESTINO (SQLite)
# ============================================

class Customer(models.Model):
    store = models.ForeignKey(
        'stores.Store',
        on_delete=models.PROTECT,
        db_column='store_id'
    )
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=50, null=True, blank=True)
    address = models.ForeignKey(
        'stores.Address',
        on_delete=models.PROTECT,
        db_column='address_id'
    )
    active = models.BooleanField(default=True)
    create_date = models.DateField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users_customer'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(
        'stores.Address',
        on_delete=models.PROTECT,
        db_column='address_id'
    )
    email = models.EmailField(max_length=50)
    store = models.ForeignKey(
        'stores.Store',
        on_delete=models.PROTECT,
        db_column='store_id'
    )
    active = models.BooleanField(default=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=255)
    last_update = models.DateTimeField()
    picture = models.BinaryField(null=True, blank=True)

    class Meta:
        db_table = 'users_staff'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
