from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Instructor



# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (('Rol personalizado', {'fields': ('is_instructor',)}),)
    add_fieldsets = BaseUserAdmin.add_fieldsets + ((None, {'fields': ('is_instructor',)}),)
    list_display = ('username', 'email', 'is_instructor', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_instructor', 'is_staff', 'is_active')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'user__email')
