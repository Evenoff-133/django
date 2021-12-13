from django.shortcuts import render
from .models import Article


def index_handler(request):
    last_articles = Article.objects.all().order_by('-pub_date')[:3]
    breakpoint()
    context = {
        'last_articles': last_articles
    }
    return render(request, 'news/index.html', context)


def blog_handler(request):
    context = {}
    return render(request, 'news/blog.html', context)


def page_handler(request):
    context = {}
    return render(request, 'news/page.html', context)


def contact_handler(request):
    context = {}
    return render(request, 'news/contact.html', context)


def about_handler(request):
    context = {}
    return render(request, 'news/about.html', context)


def search_handler(request):
    context = {}
    return render(request, 'news/search.html', context)


def robots_handler(request):
    context = {}
    return render(request, 'news/robots.txt', context,
                  content_type='text/plain')