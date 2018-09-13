from django.contrib import admin
from .models import Product, Post
# Register your models here.


def mark_as_finished(modeladmin, request, queryset):
    queryset.update(finished=True)


mark_as_finished.short_description = "Mark selected as finished"


def mark_as_expired(modeladmin, request, queryset):
    queryset.update(paid=True)


mark_as_expired.short_description = "Mark selected as expired"


def mark_as_projectpan(modeladmin, request, queryset):
    queryset.update(project_pan=True)


mark_as_projectpan.short_description = "Mark selected as Project pan"


def mark_as_posted(modeladmin, request, queryset):
    queryset.update(posted=True)


mark_as_posted.short_description = "Mark selected as posted"


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
    list_filter = ['project_pan', 'category', 'brand']
    actions = [mark_as_finished,
               mark_as_expired,
               mark_as_projectpan,
               mark_as_posted]


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
