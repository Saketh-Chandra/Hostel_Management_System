from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'hostelapp/home.html')


def sam(request):
    return render(request, 'hostelapp/sample.html')


def floor(request):
    return render(request, 'hostelapp/floor.html')


def rooms(request):
    return render(request, 'hostelapp/rooms.html')


def student(request):
    return render(request, 'hostelapp/student.html')


def warden(request):
    return render(request, 'hostelapp/warden.html')
