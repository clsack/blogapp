#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 20:53:23 2018

@author: carol
"""

from .models import Product, Post
import django_filters


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category']


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['brand']
