from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def account_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    context = {'title': 'Login'}
    return render(request, 'login.html', context)



def account_logout(request):
    logout(request)
    return redirect('account_login') 