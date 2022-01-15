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
    path('', views.IndexView.as_view(), name='homepage'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('category/<cat_slug>', views.CategoryListView.as_view(), name='category'),

    path('post/<post_slug>', views.PageDetailView.as_view(), name='article'),

    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('search/', views.SearchView.as_view(), name='search'),

    path('robots.txt', views.RobotsView.as_view()),

    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),

    # grappelli URLS
    path('grappelli/', include('grappelli.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
