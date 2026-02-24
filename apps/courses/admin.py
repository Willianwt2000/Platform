from django.contrib import admin
from .models import category,course,enrollment,module,progress,review

# Register your models here.
@admin.register(category.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(course.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'slug', 'overview', 'created_at', 'categories_display')
    search_fields = ('title', 'user__owner')
    list_filter = ('categories', 'created_at')

    def categories_display(self, obj):
        """Show comma-separated categories for a course (ManyToMany)."""
        return ", ".join([c.name for c in obj.categories.all()])
    categories_display.short_description = 'Categories'

@admin.register(enrollment.Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    search_fields = ('user__owner', 'course__title')
    list_filter = ('enrolled_at',)

@admin.register(module.Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'description')
    search_fields = ('course__title', 'title')
    list_filter = ('course',)

@admin.register(progress.Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'progress', 'updated_at')
    search_fields = ('user__username', 'course__title')
    list_filter = ('updated_at',)

@admin.register(review.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'created_at')
    search_fields = ('user__username', 'course__title')
    list_filter = ('rating', 'created_at')