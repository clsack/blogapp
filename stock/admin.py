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

def mark_as_posted(modeladmin, request, queryset):
    queryset.update(posted=True)


mark_as_posted.short_description = "Mark selected posts as published"

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product',
                    'brand',
                    'collection',
                    'category',
                    'finish',
                    'color',
                    'bought_date',
                    'expiration_date',
                    'currency',
                    'price',
                    'duration',
                    'quality',
                    'project_pan',
                    'percentage_used',
                    'finished',
                    'posted',
                    'picture'
                    ]
    ordering = ['product', 'brand', 'category']
    actions = [mark_as_finished, mark_as_expired]


admin.site.register(Product, ProductAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'brand',
                    'tags',
                    'hashtags',
                    'posted',
                    'link',
                    'short',
                    'date',
                    'ig',
                    'co']
    ordering = ['-date']
    actions = [mark_as_posted]


admin.site.register(Post, PostAdmin)
