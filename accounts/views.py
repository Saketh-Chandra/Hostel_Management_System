from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
import re


# Create your views here.

def hello_world(request):
    return HttpResponse(f"<h3>Hello {request.user}!</h3>")


@unauthenticated_user
def login_views(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('user_page')
            return HttpResponse(f'hello {request.user}')
        else:
            messages.info(request, "username or password is incorrect")
    context = {}
    return render(request, 'accounts/loginPage.html', context)


@unauthenticated_user
def register_views(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save(commit=False)
            user.save()
            user_email = form.cleaned_data.get('email')
            students = re.findall('students', user_email)
            warden = re.findall('warden', user_email)
            print(user_email, type(user_email), '--------------------------')
            print('students' in students)
            if 'students' in students:
                # print('hello student')
                user_group = Group.objects.get(name='student')
                user.groups.add(user_group)
            elif 'warden' in warden:
                # print('hello warden')
                user_group = Group.objects.get(name='warden')
                user.groups.add(user_group)
            else:
                # print('error')
                messages.error(request, 'its not a correct email!')
                return redirect('register_page')
            user_name = form.cleaned_data.get('username')
            # print(user_name)
            messages.success(request, 'Account was successfully created for ' + user_name)
            return redirect('login_page')
    context = {'form': form}
    return render(request, 'accounts/registerPage.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You are successfully logged out')
    return redirect('login_page')
