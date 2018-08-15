from django.contrib import admin
from .models import Product, Post
from datetime import datetime
# Register your models here.


def mark_as_finished(modeladmin, request, queryset):
    queryset.update(completed=True, date_completed=datetime.now())


mark_as_finished.short_description = "Mark selected products as finished"


def mark_as_expired(modeladmin, request, queryset):
    queryset.update(paid=True)


mark_as_expired.short_description = "Mark selected products as expired"


class ProductAdmin(admin.ModelAdmin):
    list_display = ['brand', 'product', 'collection', 'completed']
    ordering = ['date_scheduled']
    actions = [mark_as_finished, mark_as_expired]


admin.site.register(Product, ProductAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['expense_text', 'date_scheduled', 'amount', 'currency', 'paid']
    ordering = ['date_scheduled']
    actions = [mark_as_published]


admin.site.register(Post, PostAdmin)
