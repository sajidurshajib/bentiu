from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from notices.models import Notice
from news.models import News

# Create your views here.
def main(request):
    news = News.objects.order_by('-created_at')
    paginator = Paginator(news, 3)  
    try:
        news = paginator.page(1)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {'title': 'BENTIU University', 'news':news}
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


def news(request):
    news = News.objects.order_by('-created_at')
    
    page = request.GET.get('page')
    limit = request.GET.get('limit', 6)
    paginator = Paginator(news, limit)  
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

        
    context = {'title': 'News', 'news': news}
    return render(request, 'news.html', context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    context = {'news': news}
    return render(request, 'news_detail.html', context)

def contacts(request):
    context = {'title': 'Contact Us'}
    return render(request, 'contact.html', context)