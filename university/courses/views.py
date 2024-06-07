from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Courses
from .forms import CoursesForm

@login_required(login_url='/account')
def courses(request):
    cr = Courses.objects.order_by('-created_at')
    
    page = request.GET.get('page')
    limit = request.GET.get('limit', 10)
    paginator = Paginator(cr, limit)  
    try:
        cr = paginator.page(page)
    except PageNotAnInteger:
        cr = paginator.page(1)
    except EmptyPage:
        cr = paginator.page(paginator.num_pages)

        
    context = {'title': 'Courses', 'courses': cr}
    return render(request, 'dashboard/courses.html', context)


@login_required(login_url='/account')
def course_add(request):

    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-courses')
        
    else:
        form = CoursesForm()
        context = {'title': 'Add Course', 'form': form}
        return render(request, 'dashboard/course-add.html', context)
    


def course_edit(request, id):
    course = get_object_or_404(Courses, pk=id)

    if request.method == 'POST':
        form = CoursesForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('dashboard-courses')
    else:
        form = CoursesForm(instance=course)

    context = {'form': form, 'course': course}
    return render(request, 'dashboard/course-edit.html', context)



@login_required(login_url='/account')
def course_remove(request, id):
    cr = get_object_or_404(Courses, id=id)
    cr.delete()
    return redirect('dashboard-courses') 