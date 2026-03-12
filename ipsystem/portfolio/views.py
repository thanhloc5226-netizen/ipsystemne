from django.shortcuts import render
from portfolio.models import *

# Create your views here.
def portfolio(request):
    category = Category.objects.all()
    portfolio = Portfolio.objects.all().order_by('category')
    for p in portfolio:
        p.cat_slug = CAT_SLUG.get(p.category.name, 'other')
    context = {
        'category': category,
        'portfolio': portfolio,
    }
    return render(request, 'portfolio/portfolio.html',context)

def project(request,id):
    portfolio = Portfolio.objects.get(id=id)
    return render(request, 'portfolio/project.html', {'portfolio': portfolio})

# SLUG
CAT_SLUG = {
    'Thương mại điện tử': 'tmdt',
    'Giới thiệu doanh nghiệp': 'dn',
    'Landing Page': 'lp',
}