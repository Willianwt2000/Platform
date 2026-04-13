from django.contrib import admin
from  .models import Rental,Payment

# Register your models here.
admin.site.register(Rental)
admin.site.register(Payment)