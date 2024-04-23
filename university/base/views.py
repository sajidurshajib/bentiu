from django.shortcuts import render

# Create your views here.
def main(request):
    context = {'title': 'BENTIU University'}
    return render(request, 'main.html', context)


def about(request):
    context = {'title': 'About'}
    return render(request, 'about.html', context)


def cources(request):
    context = {'title': 'Cources'}
    return render(request, 'cources.html', context)


def contacts(request):
    context = {'title': 'Contact Us'}
    return render(request, 'contact.html', context)