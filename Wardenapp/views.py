from django.shortcuts import render, redirect
from hostelapp.models import *
from .filters import *
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'Wardenapp/home.html')


def blocks_view(request):
    wardenname = warden.objects.filter(Warden_ID=request.user)
    print(wardenname, request.user)
    context = {'warden': wardenname}
    return render(request, 'Wardenapp/blocks.html', context)


'''def floors(request,pk):
    #wardenname=warden.objects.filter(Warden_ID=request.user)
    block_tem = blocks.objects.filter(id=pk)
    floorname=block_tem.floors_set.all()
    context={'floors':floorname}
    return render(request,'Wardenapp/floors.html',context)'''


def floors_view(request, pk):
    print(pk)
    # block_tem = blocks.objects.filter(id=pk)
    floor_list = floors.objects.filter(id=pk)
    print(floor_list)
    context = {'floor_list': floor_list}
    return render(request, 'Wardenapp/floors.html', context)


def rooms_view(request, pk):
    print(pk)
    floor_tem = floors.objects.get(id=pk)
    room_list = floor_tem.room_set.all()
    print(room_list)
    myFilter=roomFilter(request.GET,queryset=room_list)
    room_list=myFilter.qs
    context = {'room_list': room_list,'myFilter':myFilter}
    return render(request, 'Wardenapp/rooms.html', context)


def student_view(request, pk):

    student_list = student_room.objects.filter(user_room_id=pk)
    myFilter=student_roomFilter(request.GET,queryset=student_list)
    student_list=myFilter.qs
    context = {'student_list': student_list,'myFilter':myFilter}
    print(student_list)
    return render(request, 'Wardenapp/student_rooms.html', context)
