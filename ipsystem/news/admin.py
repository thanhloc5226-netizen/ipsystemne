from django.contrib import admin

from news.models import *

# Register your models here.
admin.site.register(NewsType)
admin.site.register(NewsDetail)
