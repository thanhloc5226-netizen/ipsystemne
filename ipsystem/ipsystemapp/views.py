
from django.shortcuts import render
from .models import CarouselSlide, HeroSection
from portfolio.models import *
# Create your views here.


def home(request):
    slides = CarouselSlide.objects.filter(is_active=True).order_by('order')
    hero = HeroSection.objects.filter(is_active=True).first()
    portfolio = Portfolio.objects.all()

    context = {
        'slides': slides,
        'hero': hero,
        'portfolio': portfolio,
        'title': 'Trang chủ',
    }
    return render(request, 'ipsystemapp/home.html', context)










