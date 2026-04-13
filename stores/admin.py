from django.contrib import admin
from  .models import Country,City,Address,Store
# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Store)
