from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account')
def dashboard(request):
    context = {'title': 'Dashboard'}
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='/account')
def profile(request):
    context = {'title': 'Profile'}
    return render(request, 'dashboard/profile.html', context)
