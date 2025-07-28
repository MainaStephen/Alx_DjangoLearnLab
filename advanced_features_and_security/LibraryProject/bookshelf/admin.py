from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Displayed columns
    list_filter = ('publication_year',)  # Sidebar filter
    search_fields = ('title', 'author')  # Search bar
