from django.shortcuts import render,redirect
from . form import LoginForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def dashboardview(request):
    return render(request, 'account/dashboard.html')

def loginview(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    context['loginform'] = form
    return render(request, 'account/login.html', context)

def logoutview(request):
    logout(request)
    return redirect('index')

# Dashboard
def order(request):
    return render(request, 'dashboard/order.html')
