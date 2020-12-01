from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from accounts.decorators import *


# Create your views here.
@allowed_users(allowed_roles=['student'])
def home_view_student(request):
    info = student_room.objects.filter(user=request.user)
    context = {'data_info': info}
    # print(info, '-------')
    for i in info:
        print(i.user_room_id,i.id)
    return render(request, 'hostelapp/home.html', context=context)


@allowed_users(allowed_roles=['student'])
@is_student_booked
def block_views(request):
    print(request.user.groups.all()[0])
    blocks_list = blocks.objects.all()
    context = {'blocks_list': blocks_list}
    return render(request, 'hostelapp/block_page.html', context=context)


# def sam(request):
#     return render(request, 'hostelapp/sample.html')


@allowed_users(allowed_roles=['student'])
@is_student_booked
def floor(request, pk):
    print(pk)
    block_tem = blocks.objects.get(id=pk)
    floor_list = block_tem.floors_set.all()
    print(floor_list)
    context = {'floor_list': floor_list}

    return render(request, 'hostelapp/floor.html', context)


@allowed_users(allowed_roles=['student'])
@is_student_booked
def rooms(request, pk):
    floor_tem = floors.objects.get(id=pk)
    room_list = floor_tem.room_set.all()
    context = {'roomlist': room_list}

    return render(request, 'hostelapp/rooms.html', context)


@allowed_users(allowed_roles=['student'])
@is_student_booked
def booking_form_views(request, pk):
    room_booked = room.objects.get(id=pk)
    floor_id = room_booked.Floor_Number_id
    print("Floor Id is", floor_id)
    # booking_form = Booking_form()
    room_number = room_booked.Room_No
    floor_number = room_booked.Floor_Number
    block_name = room_booked.Block_Name
    capacity = room_booked.Capacity
    occupied = room_booked.Number_already_occupied
    print("Occupied is", occupied)
    print("Capacity is", capacity)
    try:
        if request.method == 'POST':
            print(request.method)
            if capacity > occupied:
                confirmation = student_room()
                confirmation.user = request.user
                confirmation.user_room = room_booked
                room_booked.Number_already_occupied += 1
                room_booked.save()
                confirmation.save()
                message = 'Your Booking is Confirmed'
                messages.success(request, message)
                print(message)
                return redirect('home')
            else:
                message = "Room already Filled"
                messages.error(request, message)
                print(message)
                # url = 'rooms/floor_id/'
                return redirect('rooms', pk=floor_id)
    except:
        message = "You already Booked the Room One can Book Only one Room"
        messages.error(request, message)
        return redirect('home')

    context = {'room_number': room_number, 'floor_number': floor_number, 'block_name': block_name}
    return render(request, 'hostelapp/Booking_form_page.html', context)



