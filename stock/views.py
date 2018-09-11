from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Count

# Bokeh
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

from .models import Product, Post
from .constants import CATEGORY


def index(request):
    return render(request, 'index.html')


class ProductCreate(CreateView):
    model = Product
    fields = ['product',
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
    template_name = 'products/form.html'


class ProductUpdate(UpdateView):
    model = Product
    fields = ['product',
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
    template_name = 'products/form.html'


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('index')
    template_name = 'products/confirm_delete.html'


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'


class NonfinishedListView(ListView):
    context_object_name = 'product_list'
    queryset = Product.objects.filter(finished=False)
    template_name = 'products/list.html'


class ProjectPanListView(ListView):
    context_object_name = 'product_list'
    queryset = Product.objects.filter(project_pan=True)
    template_name = 'products/list.html'


class ProductGraph(generic.DetailView):
    model = Product
    template_name = 'product/product_graph.html'

    def simple_chart(request):
        categories = CATEGORY

        count = Product.objects.annotate(num=Count('category'))

        plot = figure(x_range=categories,
                      plot_height=250,
                      title="Stock for category",
                      toolbar_location=None,
                      tools="")

        plot.vbar(x=categories, top=count, width=0.9)

        plot.xgrid.grid_line_color = None
        plot.y_range.start = 0

        script, div = components(plot, CDN)

        return render(request,
                      "products/product_graph.html",
                      {"the_script": script, "the_div": div})


class PostCreate(CreateView):
    model = Post
    fields = ['title',
              'brand',
              'product',
              'tags',
              'hashtags',
              'posted',
              'link',
              'short',
              'date',
              'ig',
              'co']
    template_name = 'posts/form.html'


class PostUpdate(UpdateView):
    model = Post
    fields = ['title',
              'posted',
              'link',
              'short',
              'date',
              'ig',
              'co']
    template_name = 'posts/form.html'


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('index')
    template_name = 'posts/confirm_delete.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context


class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'


class PostedListView(ListView):
    context_object_name = 'post_list'
    queryset = Product.objects.filter(posted=True)
    template_name = 'posts/list.html'


class DraftListView(ListView):
    context_object_name = 'post_list'
    queryset = Product.objects.filter(posted=False)
    template_name = 'posts/list.html'
