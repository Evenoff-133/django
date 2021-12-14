"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static

from news import views

urlpatterns = [
    path('', views.index_handler, name='homepage'),
    path('blog/', views.blog_handler, name='blog'),
    path('<cat_slug>', views.blog_handler, name='category'),
    path('post/<post_slug>', views.page_handler, name='article'),

    path('about/', views.about_handler, name='about'),
    path('contact/', views.contact_handler, name='contact'),
    path('search/', views.search_handler, name='search'),

    path('robots.txt', views.robots_handler),

    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += [ path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
