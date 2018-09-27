from django.contrib import admin
from .models import Product, Post
# Register your models here.


def mark_as_finished(modeladmin, request, queryset):
    queryset.update(finished=True)
    queryset.update(percentage_used=100)


mark_as_finished.short_description = "Mark selected as finished"


def mark_as_expired(modeladmin, request, queryset):
    queryset.update(paid=True)


mark_as_expired.short_description = "Mark selected as expired"


def mark_as_projectpan(modeladmin, request, queryset):
    queryset.update(project_pan=True)


mark_as_projectpan.short_description = "Mark selected as Project pan"


def mark_as_publishedig(modeladmin, request, queryset):
    queryset.update(ig=True)


mark_as_publishedig.short_description = "Published on Instagram"


def mark_as_posted(modeladmin, request, queryset):
    queryset.update(status='1')


mark_as_posted.short_description = "Mark selected as posted"


def generate_hashtags(modeladmin, request, queryset):
    queryset.update(hashtags=generate_hashtags(modeladmin.product))


generate_hashtags.short_description = "Generate hashtags"


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
                    'status',
                    'image'
                    ]
    ordering = ['category', 'brand', 'product']
    list_filter = ['finished', 'project_pan', 'category', 'brand']
    actions = [mark_as_finished,
               mark_as_expired,
               mark_as_projectpan,
               mark_as_posted]


admin.site.register(Product, ProductAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'brand',
                    'product',
                    'hashtags',
                    'link',
                    'date',
                    'status',
                    'ig',
                    'co']
    ordering = ['-date']
    list_filter = ['ig', 'brand']
    actions = [generate_hashtags, mark_as_publishedig]


admin.site.register(Post, PostAdmin)
