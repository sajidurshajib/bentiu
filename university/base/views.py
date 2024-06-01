from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from notices.models import Notice
from news.models import News
from schools.models import Schools

# Create your views here.
def main(request):
    # news  
    news = News.objects.order_by('-created_at')
    paginator = Paginator(news, 3)  
    try:
        news = paginator.page(1)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    # schools 
    schools = Schools.objects.order_by('position')
    
    context = {'title': 'BENTIU University', 'news':news, 'schools': schools}
    return render(request, 'main.html', context)


def about(request):
    context = {'title': 'About'}
    return render(request, 'about.html', context)


def schools(request):
    sc = Schools.objects.order_by('position')
    
    page = request.GET.get('page')
    limit = request.GET.get('limit', 6)
    paginator = Paginator(sc, limit)  
    try:
        sc = paginator.page(page)
    except PageNotAnInteger:
        sc = paginator.page(1)
    except EmptyPage:
        sc = paginator.page(paginator.num_pages)
        
    context = {'title': 'Schools', 'schools': sc}
    return render(request, 'schools.html', context)

def schools_detail(request, slug):
    schools = get_object_or_404(Schools, slug=slug)
    context = {'schools': schools}
    return render(request, 'schools_detail.html', context)

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