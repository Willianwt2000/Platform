from django.db import models


# ============================================
# MODELOS FUENTE (PostgreSQL - solo lectura)
# ============================================

class FilmSource(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField()
    language_id = models.IntegerField()
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.IntegerField()
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=10)
    last_update = models.DateTimeField()
    special_features = models.TextField(blank=True, null=True)
    fulltext = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'film'
        managed = False


class CategorySource(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'category'
        managed = False


class LanguageSource(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'language'
        managed = False


class FilmCategorySource(models.Model):
    film_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'film_category'
        managed = False


class FilmActorSource(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    film_id = models.IntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'film_actor'
        managed = False


class ActorSource(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'actor'
        managed = False


# ============================================
# MODELOS DESTINO (SQLite)
# ============================================

class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'language'
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

    def __str__(self):
        return self.name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'actor'
        verbose_name = 'Actor/Actriz'
        verbose_name_plural = 'Actores/Actrices'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField()
    language = models.ForeignKey(
        Language,
        on_delete=models.PROTECT,
        db_column='language_id',
        to_field='language_id'
    )
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.IntegerField()
    replacement_cost = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.CharField(max_length=10)
    last_update = models.DateTimeField(auto_now=True)
    special_features = models.TextField(blank=True, null=True)
    fulltext = models.TextField(blank=True, null=True)

    # Relaciones ManyToMany a traves de tablas intermedias
    actors = models.ManyToManyField(
        Actor,
        through='FilmActor',
        related_name='films'
    )
    categories = models.ManyToManyField(
        Category,
        through='FilmCategory',
        related_name='films'
    )

    class Meta:
        db_table = 'film'
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'

    def __str__(self):
        return self.title


class FilmActor(models.Model):
    film_actor_id = models.AutoField(primary_key=True)
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
        db_column='actor_id',
        to_field='actor_id'
    )
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        db_column='film_id'
    )
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film_actor'
        verbose_name = 'Actor de Pelicula'
        verbose_name_plural = 'Actores de Peliculas'
        unique_together = ['actor', 'film']

    def __str__(self):
        return f"{self.actor} - {self.film}"


class FilmCategory(models.Model):
    film_category_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        db_column='film_id'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        db_column='category_id',
        to_field='category_id'
    )
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film_category'
        verbose_name = 'Categoria de Pelicula'
        verbose_name_plural = 'Categorias de Peliculas'
        unique_together = ['film', 'category']

    def __str__(self):
        return f"{self.film} - {self.category}"
