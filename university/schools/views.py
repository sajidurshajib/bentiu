from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Schools
from .forms import SchoolsForm



@login_required(login_url='/account')
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
    return render(request, 'dashboard/schools.html', context)


@login_required(login_url='/account')
def schools_add(request):

    if request.method == 'POST':
        form = SchoolsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-schools')
        
    else:
        form = SchoolsForm()
        context = {'title': 'Add Schools', 'form': form}
        return render(request, 'dashboard/schools-add.html', context)


def schools_edit(request, id):
    schools = get_object_or_404(Schools, pk=id)

    if request.method == 'POST':
        form = SchoolsForm(request.POST, request.FILES, instance=schools)
        if form.is_valid():
            form.save()
            return redirect('dashboard-schools')
    else:
        form = SchoolsForm(instance=schools)

    context = {'form': form, 'schools': schools}
    return render(request, 'dashboard/schools-edit.html', context)


@login_required(login_url='/account')
def schools_remove(request, id):
    schools = get_object_or_404(Schools, id=id)
    schools.delete()
    return redirect('dashboard-schools') 