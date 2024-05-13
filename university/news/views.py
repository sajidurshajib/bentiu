from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News
from .forms import NewsForm


@login_required(login_url='/account')
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
    return render(request, 'dashboard/news.html', context)


@login_required(login_url='/account')
def news_add(request):

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-news')
        
    else:
        form = NewsForm()
        context = {'title': 'Add News', 'form': form}
        return render(request, 'dashboard/news-add.html', context)


def news_edit(request, id):
    news = get_object_or_404(News, pk=id)

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('dashboard-news')
    else:
        form = NewsForm(instance=news)

    context = {'form': form, 'news': news}
    return render(request, 'dashboard/news-edit.html', context)




@login_required(login_url='/account')
def news_remove(request, id):
    notice = get_object_or_404(News, id=id)
    notice.delete()
    return redirect('dashboard-news') 