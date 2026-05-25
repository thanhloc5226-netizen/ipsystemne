from django.shortcuts import render
from news.models import *
# Create your views here.
def index(request):
    news = NewsDetail.objects.all().order_by('-published_date')
    return render(request, 'news/news.html', {'news': news})