"""ccblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Coder's Community Admin"
admin.site.site_title = "CC Admin Panel"
admin.site.index_title = "Welcome to CC Admin Panel"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('myblog/',include('home.urls')),
    path('signup/',include('home.urls')),
    path('login/', include('home.urls')),
    path('blogpost/', include('home.urls')),
    path('search/', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)