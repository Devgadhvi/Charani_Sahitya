from django.contrib import admin
from django.utils.html import format_html
from .models import Author, Category, Song, Book, Story, User

admin.site.register(User)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'birth_date', 'death_date', 'created_at')
    list_filter = ('region', 'created_at')
    search_fields = ('name', 'biography', 'region')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'biography')
        }),
        ('Dates', {
            'fields': ('birth_date', 'death_date')
        }),
        ('Location', {
            'fields': ('region',)
        })
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'region', 'language', 'view_count', 'created_at')
    list_filter = ('category', 'region', 'language', 'created_at')
    search_fields = ('title', 'content', 'lyrics', 'author__name')
    autocomplete_fields = ['author', 'category']
    date_hierarchy = 'created_at'
    
    def view_count(self, obj):
        return format_html('<strong>{}</strong> views', obj.views)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'category')
        }),
        ('Content', {
            'fields': ('content', 'lyrics', 'translation')
        }),
        ('Media', {
            'fields': ('audio_file',)
        }),
        ('Metadata', {
            'fields': ('region', 'language')
        })
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'language', 'publication_date', 'view_count')
    list_filter = ('category', 'language', 'created_at')
    search_fields = ('title', 'description', 'author__name')
    autocomplete_fields = ['author', 'category']
    date_hierarchy = 'created_at'
    
    def view_count(self, obj):
        return format_html('<strong>{}</strong> views', obj.views)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'category')
        }),
        ('Content', {
            'fields': ('description', 'publication_date')
        }),
        ('Media', {
            'fields': ('pdf_file', 'cover_image')
        }),
        ('Metadata', {
            'fields': ('language',)
        })
    )

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'region', 'view_count', 'created_at')
    list_filter = ('category', 'region', 'created_at')
    search_fields = ('title', 'content', 'author__name')
    autocomplete_fields = ['author', 'category']
    date_hierarchy = 'created_at'
    
    def view_count(self, obj):
        return format_html('<strong>{}</strong> views', obj.views)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'category')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Metadata', {
            'fields': ('region',)
        })
    )