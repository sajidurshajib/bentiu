from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from notices.models import Notice
from news.models import News
from schools.models import Schools


def get_common_data(request):
    # news  
    news = News.objects.all().order_by('-created_at')[:3]
    #notice
    notice = Notice.objects.all().order_by('-created_at')[:3]
    # schools 
    schools = Schools.objects.order_by('position')
    
    context = {'news':news, 'schools': schools, 'notice':notice}
    return context  

def main(request):
    data = get_common_data(request=request)
    sc = Schools.objects.order_by('position')
    context = {'title': 'BENTIU University', 'all_schools': sc}
    context.update(data)
    return render(request, 'main.html', context)


def about(request):
    data = get_common_data(request=request)
    context = {'title': 'About'}
    context.update(data)
    return render(request, 'about.html', context)

def vc(request):
    data = get_common_data(request=request)
    context = {'title': 'Word of VC'}
    context.update(data)
    return render(request, 'word_of_vc.html', context)


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

    data = get_common_data(request=request)        
    context = {'title': 'Schools', 'all_schools': sc}
    context.update(data)
    return render(request, 'schools.html', context)

def schools_detail(request, slug):
    school = get_object_or_404(Schools, slug=slug)
    data = get_common_data(request=request)
    context = {'school': school}
    context.update(data)
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

    data = get_common_data(request=request)    
    context = {'title': 'Announcement', 'notices': notices}
    context.update(data)
    return render(request, 'notices.html', context)

def notice_detail(request, slug):
    single_notice = get_object_or_404(Notice, slug=slug)
    data = get_common_data(request=request)
    context = {'single_notice': single_notice}
    context.update(data)
    return render(request, 'notice_detail.html', context)


def news(request):
    all_news = News.objects.order_by('-created_at')
    
    page = request.GET.get('page')
    limit = request.GET.get('limit', 6)
    paginator = Paginator(news, limit)  
    try:
        all_news = paginator.page(page)
    except PageNotAnInteger:
        all_news = paginator.page(1)
    except EmptyPage:
        all_news = paginator.page(paginator.num_pages)
    
    data = get_common_data(request=request)
    context = {'title': 'News', 'all_news': all_news}
    context.update(data)

    return render(request, 'news.html', context)

def news_detail(request, slug):
    data = get_common_data(request=request)
    single_news = get_object_or_404(News, slug=slug)
    context = {'single_news': single_news}
    context.update(data)
    return render(request, 'news_detail.html', context)

def contacts(request):    
    data = get_common_data(request=request)
    context = {'title': 'Contact Us'}
    context.update(data)
    return render(request, 'contact.html', context)