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
            return redirect('default_home_name')
            # return HttpResponse(f'hello {request.user}')
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
                user.delete()
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


def default_home(request):
    print('default_home')
    group = None
    if request.user.is_anonymous:
        return redirect('login_page')
    else:
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            print(group)

            if group == 'student':
                return redirect('home')

            elif group == 'warden':
                return redirect('warden_blocks')
                # return view_func(request, *args, **kwargs)
            elif group == 'chief warden':
                return redirect('cheif_warden_home')
            else:
                message = "You are not authorized to view this page"
                messages.error(request, message)
                return redirect('logout_page')
                # return HttpResponse('You are not authorized to view this page')
