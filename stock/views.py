from django.conf import settings
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy

from .blogger import Credentials

import math
import os
import re
import urllib

from bokeh.embed import components
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.palettes import Plasma256
from bokeh.plotting import figure
from dateutil import parser
from googleapiclient import discovery
import itertools

from .models import Product, Post
from .constants import ACCESORIES, SKINCARE, NAILPOLISH, MAKEUP, PARFUM, STATIONERY, OTHER
from .filters import ProductFilter, PostFilter


# @login_required(login_url='/login/')
@login_required
def index(request):
    return render(request, 'index.html')


def logout(request):
    auth_logout(request)
    return redirect('index')


def login(request):
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


def product_graph(request):
    queryset = Product.objects.filter(finished=False)\
                .exclude(category__in=NAILPOLISH)\
                .exclude(category__in=STATIONERY)\
                .exclude(category__in=PARFUM)\
                .exclude(category__in=OTHER)\
                .values('category')\
                .annotate(total=Count('category'))\
                .order_by('category')
    categories = [cat['category'] for cat in queryset]
    count = [cat['total'] for cat in queryset]
    bars = len(categories)
    colors = itertools.cycle(Plasma256)
    palette = []
    for m, color in zip(range(bars), colors):
        palette.append(color)
    source = ColumnDataSource(data=dict(categories=categories,
                                        count=count,
                                        color=palette))
    title = "Stock for category"
    hover = HoverTool(tooltips=[
            ("Category", "@categories"),
            ("Count", "@count"),
            ])
    plot = figure(title=title,
                  x_range=categories,
                  plot_height=500,
                  plot_width=1500,
                  toolbar_location=None,
                  tools=[hover])

    plot.vbar(x='categories',
              top='count',
              bottom=0,
              width=0.9,
              color='color',
              source=source)

    plot.y_range.start = 0
    plot.xaxis.major_label_orientation = math.pi/4

    script, div = components(plot)

    return render_to_response("products/product_graph.html",
                              {"the_script": script, "the_div": div})


@staticmethod
def report_makeup():
    return (Product.objects.filter(finished=False)
                   .filter(category__in=MAKEUP)
                   .values('category')
                   .annotate(total=Count('category'))
                   .order_by('category'))


def report_skincare():
    return (Product.objects.filter(finished=False)
                   .filter(category__in=SKINCARE)
                   .values('category')
                   .annotate(total=Count('category'))
                   .order_by('category'))


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
            extract_url = re.findall('src="(.*?)"', post['content'], re.DOTALL)
            if extract_url:
                img_url = extract_url[0]
            else:
                img_url = ''
            file_save_dir = 'media/post'
            if any(ext in img_url for ext in settings.EXTENTIONSCHECK):
                filename = urllib.parse.urlparse(img_url).path.split('/')[-1]
                urllib.request.urlretrieve(img_url,
                                           os.path.join(file_save_dir,
                                                        filename))
            else:
                filename = 'default-placeholder.png'
            data = Post(blogger_id=post['id'],
                        title=post['title'],
                        tags=', '.join(post['labels']),
                        link=post['url'],
                        date=parser.parse(post['published']).date(),
                        status=1,
                        image_url=img_url
                        )
            data.save()
    return render(request, 'posts/list.html')


def send_mail_post(request):
    from .views import Post
    posts = Post.objects.filter(ig=False)\
                .exclude(hashtags='')\
                .exclude(hashtags=None)
    from_email = settings.EMAIL_HOST_USER
    to = settings.EMAIL_HOST_USER
    for post in posts:
        subject = post.title
        text_content = post.title + " " + post.hashtags + " " + post.image_url

        # create the email, and attach the HTML version as well.
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.send()
