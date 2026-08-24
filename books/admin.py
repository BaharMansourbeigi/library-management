from django.contrib import admin

from .models import Author, Book, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "publish_date")


admin.site.register(Author)
admin.site.register(Category)
