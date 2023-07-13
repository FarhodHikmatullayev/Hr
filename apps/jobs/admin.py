from django.contrib import admin
from .models import Company, JobCategory, Job, Location, SubContent


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(SubContent)
class SubContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'job')
    search_fields = ('job__title', 'name')


class SubContentInlineAdmin(admin.StackedInline):
    model = SubContent
    extra = 0


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [SubContentInlineAdmin]
    list_display = ('id', 'title', 'vacancy', 'created_date')
    list_filter = ('created_date', 'gender', 'nature', 'category')
    readonly_fields = ('created_date', 'modified_date')
    search_fields = ('title', 'location__title', 'job_category__title')
    date_hierarchy = 'created_date'
    prepopulated_fields = {'slug': ('title', )}


