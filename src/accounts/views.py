from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegistrationForm


def login_view(request):

    title = 'Log In'
    form = UserLoginForm(request.POST or None)

    #When LgoIN Is Required
    #next_page = request.GET['next']

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)
        login(request, user)

        # if next_page:
        #     return redirect(next_page)

        return redirect("posts:index")

    return render(request, "accounts/form.html", {
        'form': form,
        'title': title,
    })


def register_view(request):

    title = 'Register'
    form = UserRegistrationForm(request.POST or None)

    #next_page = request.GET['next']

    if form.is_valid():

        user = form.save(commit=False)

        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

        # if next_page:
        #      return redirect(next_page)

        return redirect("posts:index")

    return render(request, "accounts/form.html", {
        'form': form,
        'title': title,
    })


def logout_view(request):
    logout(request)
    return redirect("login")