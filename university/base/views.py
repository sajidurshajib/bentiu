from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'title': 'University | Home'}
    return render(request, 'home.html', context)