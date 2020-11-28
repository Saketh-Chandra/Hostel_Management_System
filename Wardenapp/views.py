from django.shortcuts import render, redirect
from hostelapp.models import *
from .filters import *
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from accounts.decorators import *


# Create your views here.

def home(request):
    return render(request, 'Wardenapp/home.html')


@allowed_users(allowed_roles=['warden'])
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


@allowed_users(allowed_roles=['warden'])
def floors_view(request, pk):
    print(pk)
    # block_tem = blocks.objects.filter(id=pk)
    floor_list = floors.objects.filter(id=pk)
    print(floor_list)
    context = {'floor_list': floor_list}
    return render(request, 'Wardenapp/floors.html', context)


@allowed_users(allowed_roles=['warden'])
def rooms_view(request, pk):
    try:
        print(pk)
        # warden_floor = warden.objects.filter(Warden_ID=request.user, Floor_Number_id=pk)
        # print(warden_floor)
        # pk_warden = warden_floor.Floor_Number_id
        # print(pk, pk_warden)
        floor_tem = floors.objects.get(id=pk)
        room_list = floor_tem.room_set.all()
        print(room_list)
        myFilter = roomFilter(request.GET, queryset=room_list)
        room_list = myFilter.qs
        context = {'room_list': room_list, 'myFilter': myFilter}
        return render(request, 'Wardenapp/rooms.html', context)
    except Exception:
        message = "Page dose not exist or You are not authorized to view this page"
        messages.error(request, message)
        return redirect('default_home_name')

    # warden_floor = warden.objects.filter(Warden_ID=request.user).first()
    # pk_warden = warden_floor.Floor_Number_id

    # print(pk_warden,type(pk_warden),type(pk))
    # if (int(pk_warden) == int(pk)):
    #
    # else:
    #     message = "Page dose not exist or You are not authorized to view this page"
    #     messages.error(request, message)
    #     return redirect('default_home_name')


@allowed_users(allowed_roles=['warden'])
def student_view(request, pk):
    student_list = student_room.objects.filter(user_room_id=pk)
    myFilter = student_roomFilter(request.GET, queryset=student_list)
    student_list = myFilter.qs
    sroom = room.objects.get(id=pk)
    form_hide = hidden_room_form(instance=sroom)
    if request.method == 'POST':
        form_hide = hidden_room_form(request.POST, instance=sroom)
        if form_hide.is_valid():
            form_hide.save()
            message = "hidden done!"
            messages.success(request, message)
    context = {'student_list': student_list, 'myFilter': myFilter, 'form_hide': form_hide}
    print(student_list)
    return render(request, 'Wardenapp/student_rooms.html', context)
