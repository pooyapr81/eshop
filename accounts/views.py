from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'account/index.html', {'name': 'pooya'})


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('accounts:home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            print('form', form.cleaned_data)
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            if user:
                login(request, user)
                return redirect('accounts:home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, 'account/login.html', context)
