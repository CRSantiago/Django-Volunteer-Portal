from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import RegisterForm

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RegisterForm()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)