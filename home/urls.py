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
from django.urls import path
from home import views

urlpatterns = [
    path('blogComment/', views.blogComment, name='blogComment'),
    path('', views.home, name='home'),
    path('myblog/', views.myblog, name='myblog'),
    path('signup/', views.signup, name='signup'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('UserLogout/', views.UserLogout, name='UserLogout'),
    path('<str:slug>', views.blogpost, name='blogpost'),
    path('search/', views.search, name='search'),
    path('PostBlog/', views.PostBlog, name='PostBlog'),
    path('like/', views.liked_post, name='liked_post'),
    path('delete/', views.delete_record, name='delete_record'),
]
