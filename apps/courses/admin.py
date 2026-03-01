from django.contrib import admin
from .models import category,course,enrollment,module,progress,review,CourseCategory

# Register your models here.
@admin.register(category.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(course.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ('categories', 'created_at')
    search_fields = ('title', 'overview')
    prepopulated_fields = {'slug': ('title',)}

    def categories_display(self, obj):
        """Show comma-separated categories for a course (ManyToMany)."""
        return ", ".join([c.name for c in obj.categories.all()])
    categories_display.short_description = 'Categories'

@admin.register(CourseCategory)
class CourseCategory(admin.ModelAdmin):
    list_display = ['course', 'category']
    list_filter = ['category']
    search_fields = ['course__title']

@admin.register(enrollment.Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    list_filter = ('course','enrolled_at')
    search_fields = ('user__username', 'course__title')

@admin.register(module.Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'description')
    list_filter = ('title', 'course__title')

@admin.register(progress.Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'progress', 'updated_at')
    search_fields = ('user__username', 'course__title')
    list_filter = ('progress',)

@admin.register(review.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'created_at')
    search_fields = ('user__username', 'course__title')
    list_filter = ('rating', 'created_at')