from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Count
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .blogger import Credentials

from googleapiclient import discovery
import urllib
import os

# Bokeh
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from dateutil import parser
import re

from .models import Product, Post
from .constants import ACCESORIES, SKINCARE, NAILPOLISH, MAKEUP, PARFUM
from .filters import ProductFilter, PostFilter


@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')


def logout(request):
    auth_logout(request)
    return render(request, 'login.html')


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
              'status',
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
              'status',
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
    paginate_by = 20
    template_name = 'products/list.html'


class AccesoriesListView(ListView):
    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__in=ACCESORIES)\
        .exclude(finished=True)
    paginate_by = 20
    template_name = 'products/list.html'


class SkincareListView(ListView):
    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__in=SKINCARE)\
        .exclude(finished=True)
    paginate_by = 20
    template_name = 'products/list.html'


class NailpolishListView(ListView):
    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__in=NAILPOLISH)\
        .exclude(finished=True)
    paginate_by = 20
    template_name = 'products/list.html'


class MakeupListView(ListView):
    context_object_name = 'product-list'
    queryset = Product.objects.filter(category__in=MAKEUP)\
        .exclude(finished=True)
    paginate_by = 20
    template_name = 'products/list.html'


class ParfumListView(ListView):
    context_object_name = 'product_list'
    queryset = Product.objects.filter(category__in=PARFUM)\
        .exclude(finished=True)
    paginate_by = 20
    template_name = 'products/list.html'

    def search(request):
        product_list = Product.objects.all()
        product_filter = ProductFilter(request.GET, queryset=product_list)
        return render(request,
                      'products/list.html',
                      {'filter': product_filter})


class NonfinishedListView(ListView):
    context_object_name = 'product_list'
    queryset = Product.objects.exclude(finished=True)
    paginate_by = 20
    template_name = 'products/list.html'


class ProjectPanListView(ListView):
    context_object_name = 'product_list'
    queryset = Product.objects.filter(project_pan=True).exclude(finished=True)
    paginate_by = 20
    template_name = 'products/list.html'


class ProductGraph(ListView):
    context_object_name = 'product_graph'
    template_name = 'products/product_graph.html'
    queryset = Product.objects.exclude(category__in=NAILPOLISH)\
        .exclude(finished=True)

    def simple_chart(request):
        categories = ACCESORIES + SKINCARE + MAKEUP + PARFUM

        count = Product.objects.annotate(num=Count('category'))

        plot = figure(x_range=categories,
                      plot_height=250,
                      title="Stock for category",
                      toolbar_location=None,
                      tools="")

        plot.vbar(x=categories.sort(), top=count, width=0.9)

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
              'link',
              'short',
              'status',
              'date',
              'ig',
              'co']
    template_name = 'posts/form.html'


class PostUpdate(UpdateView):
    model = Post
    fields = ['title',
              'link',
              'short',
              'status',
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
    paginate_by = 20
    template_name = 'posts/list.html'


class PostedListView(ListView):
    context_object_name = 'post_list'
    queryset = Post.objects.filter(status='Published')
    paginate_by = 20
    template_name = 'posts/list.html'


class DraftListView(ListView):
    context_object_name = 'post_list'
    queryset = Post.objects.filter(status='Draft')
    paginate_by = 20
    template_name = 'posts/list.html'


def get_posts(request):
    fullposts = []
    user = request.user
    usa = user.social_auth.get(provider='google-oauth2')
    service = discovery.build('blogger', 'v3', credentials=Credentials(usa))
    blogs = service.blogs()
    posts = service.posts()
    # userblogs = blogs.listByUser(userId='self').execute()
    blog = blogs.getByUrl(url=settings.BLOG_URL).execute()
    blogposts = posts.list(blogId=blog['id'])
    while blogposts is not None:
        posts_doc = blogposts.execute()
        fullposts.append(posts_doc['items'])
        blogposts = posts.list_next(blogposts, posts_doc)
    flat_posts = [item for sublist in fullposts for item in sublist]
    for post in flat_posts:
        try:
            n = Post.objects.get(blogger_id=post['id'])
        except ObjectDoesNotExist:
            extract_urls = re.findall('src="(.*?)"', post['content'], re.DOTALL)
            if extract_urls:
                img_url = extract_urls[0]
            else:
                img_url = ''
            file_save_dir = 'media/post'
            if any(ext in img_url for ext in settings.EXTENTIONSCHECK):
                filename = urllib.parse.urlparse(img_url).path.split('/')[-1]
                urllib.request.urlretrieve(img_url, os.path.join(file_save_dir, filename))
            else:
                filename = 'default-placeholder.png'
            img = os.path.join(file_save_dir, filename)
            data = Post(blogger_id=post['id'],
                        title=post['title'],
                        tags=', '.join(post['labels']),
                        link=post['url'],
                        date=parser.parse(post['published']).date(),
                        status=1,
                        image=img,
                        image_url=img_url
                        )
            data.save()
    return render(request, 'posts/list.html')
