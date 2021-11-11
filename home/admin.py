from django.contrib import admin
from home.models import BlogPost, SearchQuery,BlogComment,Like
# Register your models here.

admin.site.register((BlogPost,BlogComment))
admin.site.register(SearchQuery)
admin.site.register(Like)
