from django.shortcuts import render, redirect
from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from stores.models import Customer
import json
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group

# Create your views here.
@unauthenticated_user
def loginPage(request):


    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Username Or password is incorrect")
    context = {}
    return render(request, 'registApp/html/login.html', context)


@unauthenticated_user
def signup(request):


    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('pass1')
            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            customer_save = Customer.objects.create(
                user=user,username=username,
                email=email, password=password,
            )
            customer_save.save()

            messages.success(request, "Account was created " + username)
            # messages.info(request, 'Password not matching')

            return redirect('login')
    context = {'form': form}

    return render(request, 'registApp/html/signup.html', context)


def logoutPage(request):
    logout(request)
    return redirect("/")


