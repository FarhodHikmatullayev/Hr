from django.contrib import admin
from .models import Category, Tag, Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    list_filter = ('created_date', 'modified_date')
    date_hierarchy = 'created_date'
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'blog', 'top_level_comment_id', 'parent_comment', 'created_date')
    list_filter = ('created_date', 'modified_date')
    readonly_fields = ('created_date', 'modified_date')
    search_fields = ('name', 'blog__title')
    date_hierarchy = 'created_date'



