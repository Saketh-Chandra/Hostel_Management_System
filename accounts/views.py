from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user

# Create your views here.

def hello_world(request):
    return HttpResponse(f"<h3>Hello {request.user}!</h3>")

@unauthenticated_user
def login_views(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            #return redirect('user_page')
            return HttpResponse(f'hello {request.user}')
        else:
            messages.info(request, "username or password is incorrect")
    context={}
    return render(request, 'accounts/loginPage.html',context)
@unauthenticated_user
def register_views(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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