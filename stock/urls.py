#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:47:44 2018

@author: carol
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
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
    path('products/all/',
         views.NonfinishedListView.as_view(),
         name='product-list'),
    path('products/all/',
         views.ProjectPanListView.as_view(),
         name='product-list'),
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
    path('posts/all/',
         views.PublishedListView.as_view(),
         name='post-list'),
    path('posts/all/',
         views.DraftListView.as_view(),
         name='post-list'),
    ]
