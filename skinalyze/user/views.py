from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'users/index.html')

def features(request):
    return render (request, 'users/features.html')

def about(request):
    return render (request, 'users/about.html')

def review(request):
    return render (request, 'users/review.html')