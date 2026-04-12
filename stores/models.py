from django.db import models


# ============================================
# MODELOS FUENTE (PostgreSQL - solo lectura)
# ============================================

class CountrySource(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'country'
        managed = False


class CitySource(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country_id = models.IntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'city'
        managed = False


class AddressSource(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city_id = models.IntegerField()
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'address'
        managed = False


class StoreSource(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff_id = models.IntegerField()
    address_id = models.IntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'store'
        managed = False


# ============================================
# MODELOS DESTINO (SQLite)
# ============================================

class Country(models.Model):
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'country'
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.country


class City(models.Model):
    city = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        db_column='country_id'
    )
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'city'
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.city


class Address(models.Model):
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        db_column='city_id'
    )
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'address'
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        return self.address


class Store(models.Model):
    manager_staff_id = models.IntegerField()
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        db_column='address_id'
    )
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'store'
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'

    def __str__(self):
        return f"Store {self.id}"
