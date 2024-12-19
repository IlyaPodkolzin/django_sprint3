from blog.models import Category, Post
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def index(request):
    template_name = 'blog/index.html'
    rev_posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {
        'post_list': rev_posts,
    }
    return render(request, template_name, context)


def post_detail(request, id):
    current_time = timezone.now()
    post = get_object_or_404(
        Post,
        pk=id,
        is_published=True,
        pub_date__lte=current_time,
        category__is_published=True
    )
    template_name = 'blog/detail.html'
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    current_time = timezone.now()
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=current_time
    ).order_by('-pub_date')
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, template_name, context)
