"""super_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static

from polls.views import index, detail
from news import views

urlpatterns = [
    path('', index ),
    path('polls/<int:question_id>/', detail),

    path('blog/', views.blog_heandler),
    path('page/', views.page_heandler),
    path('about/', views.about_heandler),
    path('contact/', views.contact_heandler),
    path('index/', views.index_heandler),
    path('search/', views.search_heandler),

    path('robots.txt', views.robots_heandler),

    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
