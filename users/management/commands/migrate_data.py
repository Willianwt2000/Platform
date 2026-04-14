from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import connections, transaction
from datetime import datetime, timezone as dt_timezone


class Command(BaseCommand):
    help = 'Migrate data from PostgreSQL to SQLite with proper foreign key resolution'

    def make_aware(self, dt):
        """Convertir datetime naive a timezone-aware"""
        if dt is None:
            return None
        if timezone.is_aware(dt):
            return dt
        return timezone.make_aware(dt)

    def handle(self, *args, **kwargs):
        # Importar modelos dentro de handle para evitar problemas de importacion circular
        from users.models import Customer, CustomerSource, Staff, StaffSource
        from movies.models import (
            Film, FilmSource, Category, CategorySource,
            Language, LanguageSource, FilmCategory, FilmCategorySource,
            FilmActor, FilmActorSource, Actor, ActorSource
        )
        from stores.models import (
            Country, CountrySource, City, CitySource,
            Address, AddressSource, Store, StoreSource
        )
        from inventory.models import Inventory, InventorySource
        from sales.models import Rental, RentalSource, Payment, PaymentSource
        from reviews.models import Review, ReviewSource

        # Diccionarios para mapear IDs origen -> IDs destino
        country_id_map = {}
        city_id_map = {}
        address_id_map = {}
        store_id_map = {}
        language_id_map = {}
        category_id_map = {}
        actor_id_map = {}
        film_id_map = {}
        inventory_id_map = {}
        customer_id_map = {}
        staff_id_map = {}
        rental_id_map = {}

        with transaction.atomic():
            # ============================================
            # LIMPIAR TABLAS DESTINO
            # Orden: tablas hijas primero (por FK), luego padres
            # ============================================
            self.stdout.write(' Clearing destination tables...')

            # Tablas con dependencias (hijas)
            Payment.objects.all().delete()
            Rental.objects.all().delete()
            Review.objects.all().delete()
            Inventory.objects.all().delete()
            FilmActor.objects.all().delete()
            FilmCategory.objects.all().delete()
            Film.objects.all().delete()
            Customer.objects.all().delete()
            Staff.objects.all().delete()
            Store.objects.all().delete()
            Address.objects.all().delete()
            City.objects.all().delete()
            Country.objects.all().delete()
            Actor.objects.all().delete()
            Language.objects.all().delete()
            Category.objects.all().delete()

            self.stdout.write(self.style.SUCCESS(' Tables cleared'))

            # ============================================
            # 1. MIGRAR COUNTRIES (sin dependencias)
            # ============================================
            self.stdout.write(' Migrating countries...')
            countries = CountrySource.objects.using('dvdental').all()
            for c in countries:
                obj = Country.objects.create(country=c.country, last_update=self.make_aware(c.last_update))
                country_id_map[c.country_id] = obj.id
            self.stdout.write(self.style.SUCCESS(f' {countries.count()} Countries migrated'))

            # ============================================
            # 2. MIGRAR CITIES (depende de Country)
            # ============================================
            self.stdout.write(' Migrating cities...')
            cities = CitySource.objects.using('dvdental').all()
            for c in cities:
                obj = City.objects.create(
                    city=c.city,
                    country_id=country_id_map.get(c.country_id),
                    last_update=self.make_aware(c.last_update)
                )
                city_id_map[c.city_id] = obj.id
            self.stdout.write(self.style.SUCCESS(f' {cities.count()} Cities migrated'))

            # ============================================
            # 3. MIGRAR ADDRESSES (depende de City)
            # ============================================
            self.stdout.write(' Migrating addresses...')
            addresses = AddressSource.objects.using('dvdental').all()
            for a in addresses:
                obj = Address.objects.create(
                    address=a.address,
                    address2=a.address2,
                    district=a.district,
                    city_id=city_id_map.get(a.city_id),
                    postal_code=a.postal_code,
                    phone=a.phone,
                    last_update=self.make_aware(a.last_update)
                )
                address_id_map[a.address_id] = obj.id
            self.stdout.write(self.style.SUCCESS(f' {addresses.count()} Addresses migrated'))

            # ============================================
            # 4. MIGRAR STORES (depende de Address)
            # ============================================
            self.stdout.write(' Migrating stores...')
            stores = StoreSource.objects.using('dvdental').all()
            for s in stores:
                obj = Store.objects.create(
                    manager_staff_id=s.manager_staff_id,
                    address_id=address_id_map.get(s.address_id),
                    last_update=self.make_aware(s.last_update)
                )
                store_id_map[s.store_id] = obj.id
            self.stdout.write(self.style.SUCCESS(f' {stores.count()} Stores migrated'))

            # ============================================
            # 5. MIGRAR LANGUAGES (sin dependencias)
            # ============================================
            self.stdout.write(' Migrating languages...')
            languages = LanguageSource.objects.using('dvdental').all()
            for l in languages:
                obj = Language.objects.create(language_id=l.language_id, name=l.name, last_update=self.make_aware(l.last_update))
                language_id_map[l.language_id] = obj.language_id
            self.stdout.write(self.style.SUCCESS(f' {languages.count()} Languages migrated'))

            # ============================================
            # 6. MIGRAR CATEGORIES (sin dependencias)
            # ============================================
            self.stdout.write(' Migrating categories...')
            categories = CategorySource.objects.using('dvdental').all()
            for c in categories:
                obj = Category.objects.create(category_id=c.category_id, name=c.name, last_update=self.make_aware(c.last_update))
                category_id_map[c.category_id] = obj.category_id
            self.stdout.write(self.style.SUCCESS(f' {categories.count()} Categories migrated'))

            # ============================================
            # 7. MIGRAR ACTORS (sin dependencias)
            # ============================================
            self.stdout.write(' Migrating actors...')
            actors = ActorSource.objects.using('dvdental').all()
            for a in actors:
                obj = Actor.objects.create(
                    actor_id=a.actor_id,
                    first_name=a.first_name,
                    last_name=a.last_name,
                    last_update=self.make_aware(a.last_update)
                )
                actor_id_map[a.actor_id] = obj.actor_id
            self.stdout.write(self.style.SUCCESS(f' {actors.count()} Actors migrated'))

            # ============================================
            # 8. MIGRAR FILMS (depende de Language)
            # ============================================
            self.stdout.write(' Migrating films...')
            films = FilmSource.objects.using('dvdental').all()
            for f in films:
                obj = Film.objects.create(
                    title=f.title,
                    description=f.description,
                    release_year=f.release_year,
                    language_id=language_id_map.get(f.language_id),
                    rental_duration=f.rental_duration,
                    rental_rate=f.rental_rate,
                    length=f.length,
                    replacement_cost=f.replacement_cost,
                    rating=str(f.rating) if f.rating else None,
                    last_update=self.make_aware(f.last_update),
                    special_features=f.special_features,
                    fulltext=f.fulltext
                )
                film_id_map[f.film_id] = obj.id
            self.stdout.write(self.style.SUCCESS(f' {films.count()} Films migrated'))

            # ============================================
            # 9. MIGRAR FILM CATEGORIES (depende de Film y Category)
            # ============================================
            self.stdout.write(' Migrating film categories...')
            film_categories = FilmCategorySource.objects.using('dvdental').all()
            for fc in film_categories:
                FilmCategory.objects.create(
                    film_id=film_id_map.get(fc.film_id),
                    category_id=category_id_map.get(fc.category_id),
                    last_update=self.make_aware(fc.last_update)
                )
            self.stdout.write(self.style.SUCCESS(f' {film_categories.count()} Film Categories migrated'))

            # ============================================
            # 10. MIGRAR FILM ACTORS (depende de Film y Actor)
            # ============================================
            self.stdout.write(' Migrating film actors...')
            film_actors = FilmActorSource.objects.using('dvdental').all()
            for fa in film_actors:
                FilmActor.objects.create(
                    actor_id=actor_id_map.get(fa.actor_id),
                    film_id=film_id_map.get(fa.film_id),
                    last_update=self.make_aware(fa.last_update)
                )
            self.stdout.write(self.style.SUCCESS(f' {film_actors.count()} Film Actors migrated'))

            # ============================================
            # 11. MIGRAR INVENTORY (depende de Film y Store)
            # ============================================
            self.stdout.write(' Migrating inventory...')
            inventories = InventorySource.objects.using('dvdental').all()
            for i in inventories:
                obj = Inventory.objects.create(
                    film_id=film_id_map.get(i.film_id),
                    store_id=store_id_map.get(i.store_id),
                    last_update=self.make_aware(i.last_update)
                )
                inventory_id_map[i.inventory_id] = obj.id
            self.stdout.write(self.style.SUCCESS(f' {inventories.count()} Inventory items migrated'))

            # ============================================
            # 12. MIGRAR CUSTOMERS (depende de Store y Address)
            # ============================================
            self.stdout.write(' Migrating customers...')
            customers = CustomerSource.objects.using('dvdental').all()
            for c in customers:
                obj = Customer.objects.create(
                    store_id=store_id_map.get(c.store_id),
                    first_name=c.first_name,
                    last_name=c.last_name,
                    email=c.email,
                    address_id=address_id_map.get(c.address_id),
                    active=c.activebool,
                    create_date=c.create_date,
                    last_update=timezone.now()
                )
                customer_id_map[c.customer_id] = obj.id
            self.stdout.write(self.style.SUCCESS(f' {customers.count()} Customers migrated'))

            # ============================================
            # 13. MIGRAR STAFF (depende de Store y Address)
            # ============================================
            self.stdout.write(' Migrating staff...')
            staff = StaffSource.objects.using('dvdental').all()
            for s in staff:
                obj = Staff.objects.create(
                    staff_id=s.staff_id,
                    first_name=s.first_name,
                    last_name=s.last_name,
                    email=s.email,
                    store_id=store_id_map.get(s.store_id),
                    address_id=address_id_map.get(s.address_id),
                    username=s.username,
                    password=s.password,
                    active=s.active,
                    last_update=timezone.now(),
                    picture=s.picture
                )
                staff_id_map[s.staff_id] = obj.staff_id
            self.stdout.write(self.style.SUCCESS(f' {staff.count()} Staff migrated'))

            # ============================================
            # 14. MIGRAR RENTALS (depende de Inventory, Customer, Staff)
            # ============================================
            self.stdout.write(' Migrating rentals...')
            rentals = RentalSource.objects.using('dvdental').all()
            for r in rentals:
                obj = Rental.objects.create(
                    rental_date=self.make_aware(r.rental_date),
                    inventory_id=inventory_id_map.get(r.inventory_id),
                    customer_id=customer_id_map.get(r.customer_id),
                    return_date=self.make_aware(r.return_date),
                    staff_id=staff_id_map.get(r.staff_id),
                    last_update=self.make_aware(r.last_update)
                )
                rental_id_map[r.rental_id] = obj.id
            self.stdout.write(self.style.SUCCESS(f' {rentals.count()} Rentals migrated'))

            # ============================================
            # 15. MIGRAR PAYMENTS (depende de Customer, Staff, Rental)
            # ============================================
            self.stdout.write(' Migrating payments...')
            payments = PaymentSource.objects.using('dvdental').all()
            for p in payments:
                Payment.objects.create(
                    customer_id=customer_id_map.get(p.customer_id),
                    staff_id=staff_id_map.get(p.staff_id),
                    rental_id=rental_id_map.get(p.rental_id),
                    amount=p.amount,
                    payment_date=self.make_aware(p.payment_date)
                )
            self.stdout.write(self.style.SUCCESS(f' {payments.count()} Payments migrated'))

            # ============================================
            # 16. MIGRAR REVIEWS (depende de Film y Customer)
            # ============================================
            self.stdout.write(' Migrating reviews...')
            reviews = ReviewSource.objects.using('dvdental').all()
            for r in reviews:
                Review.objects.create(
                    film_id=film_id_map.get(r.film_id),
                    customer_id=customer_id_map.get(r.customer_id),
                    rating=r.rating,
                    review_text=r.review_text,
                    review_date=self.make_aware(r.review_date)
                )
            self.stdout.write(self.style.SUCCESS(f' {reviews.count()} Reviews migrated'))

            # ============================================
            # FINAL
            # ============================================
            self.stdout.write(self.style.SUCCESS('\n ALL DATA MIGRATED SUCCESSFULLY!'))
