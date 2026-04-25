from django.shortcuts import render

def policies(request):
    return render(request, 'policies/termsofuse.html')

def privacy(request):
    return render(request, 'policies/privacy.html')

def payment(request):
    return render(request, 'policies/payment.html')
def return_policy(request):
    return render(request, 'policies/return_policy.html')