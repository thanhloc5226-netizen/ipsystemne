
from django.shortcuts import render
from .models import CarouselSlide, HeroSection


def home(request):
    slides = CarouselSlide.objects.filter(is_active=True).order_by('order')
    hero = HeroSection.objects.filter(is_active=True).first()

    context = {
        'slides': slides,
        'hero': hero,
    }
    return render(request, 'ipsystemapp/home.html', context)










