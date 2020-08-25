from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'post':
        print('hey thetre')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('home')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    if request.method == 'post':

        messages.error(request,'testing error')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')