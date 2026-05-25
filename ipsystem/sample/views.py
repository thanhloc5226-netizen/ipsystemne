from django.shortcuts import render

from sample.models import Sample

# Create your views here.
def index(request):
    samples = Sample.objects.all()
    return render(request, 'sample/sample.html', {'samples': samples})

def sample_detail(request, sample_id):
    sample = Sample.objects.get(id=sample_id)
    return render(request, 'sample/sample_detail.html', {'sample': sample})