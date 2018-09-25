#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:47:44 2018

@author: carol
"""

from django.urls import path
from django_filters.views import FilterView
from .filters import ProductFilter, PostFilter
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.logout, name='logout'),
    path('products/add/',
         views.ProductCreate.as_view(),
         name='product-add'),
    path('products/<int:pk>/update/',
         views.ProductUpdate.as_view(),
         name='product-update'),
    path('products/<int:pk>/delete/',
         views.ProductDelete.as_view(),
         name='product-delete'),
    path('products/<int:pk>/',
         views.ProductDetail.as_view(),
         name='product-detail'),

    path('products/all/',
         views.ProductListView.as_view(),
         name='product-list'),

    path('products/search/',
         FilterView.as_view(filterset_class=ProductFilter,
                            template_name='product-list'),
         name='product-filter'),

    path('products/accesories/',
         views.AccesoriesListView.as_view(),
         name='accesories-list'),
    path('products/skincare/',
         views.SkincareListView.as_view(),
         name='skincare-list'),
    path('products/nailpolish/',
         views.NailpolishListView.as_view(),
         name='nailpolish-list'),
    path('products/makeup/',
         views.MakeupListView.as_view(),
         name='makeup-list'),
    path('products/parfum/',
         views.ParfumListView.as_view(),
         name='parfum-list'),

    path('products/nonfinished/',
         views.NonfinishedListView.as_view(),
         name='nonfinished-list'),
    path('products/projectpan/',
         views.ProjectPanListView.as_view(),
         name='projectpan-list'),

    path('products/graph/',
         views.ProductGraph.as_view(),
         name='product-graph'),

    # Posts urls
    path('posts/add/',
         views.PostCreate.as_view(),
         name='post-add'),
    path('posts/<int:pk>/update/',
         views.PostUpdate.as_view(),
         name='post-update'),
    path('posts/<int:pk>/delete/',
         views.PostDelete.as_view(),
         name='post-delete'),
    path('posts/<int:pk>/',
         views.PostDetail.as_view(),
         name='post-detail'),
    path('posts/all/',
         views.PostListView.as_view(),
         name='post-list'),
    path('posts/posted/',
         views.PostedListView.as_view(),
         name='posted-list'),
    path('posts/draft/',
         views.DraftListView.as_view(),
         name='draft-list'),

    # Load posts
    path('posts/get_posts',
         views.get_posts,
         name='get-list'),
    ]
