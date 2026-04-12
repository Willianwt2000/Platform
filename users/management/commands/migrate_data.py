from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import connections


class Command(BaseCommand):
    help = 'Migrate data from PostgreSQL to SQLite'

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
        Country.objects.bulk_create([
            Country(country=c.country, last_update=c.last_update)
            for c in countries
        ])
        self.stdout.write(self.style.SUCCESS(f' {countries.count()} Countries migrated'))

        # ============================================
        # 2. MIGRAR CITIES (depende de Country)
        # ============================================
        self.stdout.write(' Migrating cities...')
        cities = CitySource.objects.using('dvdental').all()
        City.objects.bulk_create([
            City(city=c.city, country_id=c.country_id, last_update=c.last_update)
            for c in cities
        ])
        self.stdout.write(self.style.SUCCESS(f' {cities.count()} Cities migrated'))

        # ============================================
        # 3. MIGRAR ADDRESSES (depende de City)
        # ============================================
        self.stdout.write(' Migrating addresses...')
        addresses = AddressSource.objects.using('dvdental').all()
        Address.objects.bulk_create([
            Address(
                address=a.address,
                address2=a.address2,
                district=a.district,
                city_id=a.city_id,
                postal_code=a.postal_code,
                phone=a.phone,
                last_update=a.last_update
            )
            for a in addresses
        ])
        self.stdout.write(self.style.SUCCESS(f' {addresses.count()} Addresses migrated'))

        # ============================================
        # 4. MIGRAR STORES (depende de Address)
        # ============================================
        self.stdout.write(' Migrating stores...')
        stores = StoreSource.objects.using('dvdental').all()
        Store.objects.bulk_create([
            Store(
                manager_staff_id=s.manager_staff_id,
                address_id=s.address_id,
                last_update=s.last_update
            )
            for s in stores
        ])
        self.stdout.write(self.style.SUCCESS(f' {stores.count()} Stores migrated'))

        # ============================================
        # 5. MIGRAR LANGUAGES (sin dependencias)
        # ============================================
        self.stdout.write(' Migrating languages...')
        languages = LanguageSource.objects.using('dvdental').all()
        Language.objects.bulk_create([
            Language(name=l.name, last_update=l.last_update)
            for l in languages
        ])
        self.stdout.write(self.style.SUCCESS(f' {languages.count()} Languages migrated'))

        # ============================================
        # 6. MIGRAR CATEGORIES (sin dependencias)
        # ============================================
        self.stdout.write(' Migrating categories...')
        categories = CategorySource.objects.using('dvdental').all()
        Category.objects.bulk_create([
            Category(name=c.name, last_update=c.last_update)
            for c in categories
        ])
        self.stdout.write(self.style.SUCCESS(f' {categories.count()} Categories migrated'))

        # ============================================
        # 7. MIGRAR ACTORS (sin dependencias)
        # ============================================
        self.stdout.write(' Migrating actors...')
        actors = ActorSource.objects.using('dvdental').all()
        Actor.objects.bulk_create([
            Actor(
                actor_id=a.actor_id,
                first_name=a.first_name,
                last_name=a.last_name,
                last_update=a.last_update
            )
            for a in actors
        ])
        self.stdout.write(self.style.SUCCESS(f' {actors.count()} Actors migrated'))

        # ============================================
        # 8. MIGRAR FILMS (depende de Language)
        # ============================================
        self.stdout.write(' Migrating films...')
        films = FilmSource.objects.using('dvdental').all()
        Film.objects.bulk_create([
            Film(
                title=f.title,
                description=f.description,
                release_year=f.release_year,
                language_id=f.language_id,
                rental_duration=f.rental_duration,
                rental_rate=f.rental_rate,
                length=f.length,
                replacement_cost=f.replacement_cost,
                rating=str(f.rating) if f.rating else None,
                last_update=f.last_update,
                special_features=f.special_features,
                fulltext=f.fulltext
            )
            for f in films
        ])
        self.stdout.write(self.style.SUCCESS(f' {films.count()} Films migrated'))

        # ============================================
        # 9. MIGRAR FILM CATEGORIES (depende de Film y Category)
        # Usar SQL raw para tabla de union
        # ============================================
        self.stdout.write(' Migrating film categories...')
        with connections['dvdental'].cursor() as cursor:
            cursor.execute('SELECT film_id, category_id, last_update FROM film_category')
            rows = cursor.fetchall()
        FilmCategory.objects.bulk_create([
            FilmCategory(
                film_id=row[0],
                category_id=row[1],
                last_update=row[2]
            )
            for row in rows
        ])
        self.stdout.write(self.style.SUCCESS(f' {len(rows)} Film Categories migrated'))

        # ============================================
        # 10. MIGRAR FILM ACTORS (depende de Film y Actor)
        # ============================================
        self.stdout.write(' Migrating film actors...')
        with connections['dvdental'].cursor() as cursor:
            cursor.execute('SELECT actor_id, film_id, last_update FROM film_actor')
            rows = cursor.fetchall()
        FilmActor.objects.bulk_create([
            FilmActor(
                actor_id=row[0],
                film_id=row[1],
                last_update=row[2]
            )
            for row in rows
        ])
        self.stdout.write(self.style.SUCCESS(f' {len(rows)} Film Actors migrated'))

        # ============================================
        # 11. MIGRAR INVENTORY (depende de Film y Store)
        # ============================================
        self.stdout.write(' Migrating inventory...')
        inventories = InventorySource.objects.using('dvdental').all()
        Inventory.objects.bulk_create([
            Inventory(
                film_id=i.film_id,
                store_id=i.store_id,
                last_update=i.last_update
            )
            for i in inventories
        ])
        self.stdout.write(self.style.SUCCESS(f' {inventories.count()} Inventory items migrated'))

        # ============================================
        # 12. MIGRAR CUSTOMERS (depende de Store y Address)
        # ============================================
        self.stdout.write(' Migrating customers...')
        customers = CustomerSource.objects.using('dvdental').all()
        Customer.objects.bulk_create([
            Customer(
                store_id=c.store_id,
                first_name=c.first_name,
                last_name=c.last_name,
                email=c.email,
                address_id=c.address_id,
                active=c.activebool,
                create_date=c.create_date,
                last_update=timezone.now()
            )
            for c in customers
        ])
        self.stdout.write(self.style.SUCCESS(f' {customers.count()} Customers migrated'))

        # ============================================
        # 13. MIGRAR STAFF (depende de Store y Address)
        # ============================================
        self.stdout.write(' Migrating staff...')
        staff = StaffSource.objects.using('dvdental').all()
        Staff.objects.bulk_create([
            Staff(
                staff_id=s.staff_id,
                first_name=s.first_name,
                last_name=s.last_name,
                email=s.email,
                store_id=s.store_id,
                address_id=s.address_id,
                username=s.username,
                password=s.password,
                active=s.active,
                last_update=timezone.now(),
                picture=s.picture
            )
            for s in staff
        ])
        self.stdout.write(self.style.SUCCESS(f' {staff.count()} Staff migrated'))

        # ============================================
        # 14. MIGRAR RENTALS (depende de Inventory, Customer, Staff)
        # ============================================
        self.stdout.write(' Migrating rentals...')
        rentals = RentalSource.objects.using('dvdental').all()
        Rental.objects.bulk_create([
            Rental(
                rental_date=r.rental_date,
                inventory_id=r.inventory_id,
                customer_id=r.customer_id,
                return_date=r.return_date,
                staff_id=r.staff_id,
                last_update=r.last_update
            )
            for r in rentals
        ])
        self.stdout.write(self.style.SUCCESS(f' {rentals.count()} Rentals migrated'))

        # ============================================
        # 15. MIGRAR PAYMENTS (depende de Customer, Staff, Rental)
        # ============================================
        self.stdout.write(' Migrating payments...')
        payments = PaymentSource.objects.using('dvdental').all()
        Payment.objects.bulk_create([
            Payment(
                customer_id=p.customer_id,
                staff_id=p.staff_id,
                rental_id=p.rental_id,
                amount=p.amount,
                payment_date=p.payment_date
            )
            for p in payments
        ])
        self.stdout.write(self.style.SUCCESS(f' {payments.count()} Payments migrated'))

        # ============================================
        # 16. MIGRAR REVIEWS (depende de Film y Customer)
        # ============================================
        self.stdout.write(' Migrating reviews...')
        reviews = ReviewSource.objects.using('dvdental').all()
        Review.objects.bulk_create([
            Review(
                film_id=r.film_id,
                customer_id=r.customer_id,
                rating=r.rating,
                review_text=r.review_text,
                review_date=r.review_date
            )
            for r in reviews
        ])
        self.stdout.write(self.style.SUCCESS(f' {reviews.count()} Reviews migrated'))

        # ============================================
        # FINAL
        # ============================================
        self.stdout.write(self.style.SUCCESS('\n ALL DATA MIGRATED SUCCESSFULLY!'))
