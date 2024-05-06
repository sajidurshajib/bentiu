from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from notices.models import Notice

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

def notice(request):
    notices = Notice.objects.order_by('-created_at')
    
    page = request.GET.get('page')
    limit = request.GET.get('limit', 6)
    paginator = Paginator(notices, limit)  
    try:
        notices = paginator.page(page)
    except PageNotAnInteger:
        notices = paginator.page(1)
    except EmptyPage:
        notices = paginator.page(paginator.num_pages)

        
    context = {'title': 'Notice', 'notices': notices}
    return render(request, 'notices.html', context)

def notice_detail(request, slug):
    notice = get_object_or_404(Notice, slug=slug)
    context = {'notice': notice}
    return render(request, 'notice_detail.html', context)


def contacts(request):
    context = {'title': 'Contact Us'}
    return render(request, 'contact.html', context)