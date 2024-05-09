from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Notice
from .forms import NoticeForm


@login_required(login_url='/account')
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
    return render(request, 'dashboard/notice.html', context)


@login_required(login_url='/account')
def notice_add(request):

    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-notice')
        
    else:
        form = NoticeForm()
        context = {'title': 'Add Notice', 'form': form}
        return render(request, 'dashboard/notice-add.html', context)


def notice_edit(request, id):
    notice = get_object_or_404(Notice, pk=id)

    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('dashboard-notice')
    else:
        form = NoticeForm(instance=notice)

    context = {'form': form, 'notice': notice}
    return render(request, 'dashboard/notice-edit.html', context)



@login_required(login_url='/account')
def notice_remove(request, id):
    notice = get_object_or_404(Notice, id=id)
    notice.delete()
    return redirect('dashboard-notice') 