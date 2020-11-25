from django.db.models import F
from django.shortcuts import render, redirect
from hostelapp.models import *
from .forms import *
from django.conf import settings
from accounts.decorators import *

User = settings.AUTH_USER_MODEL


# Create your views here.
@allowed_users(allowed_roles=['chief warden'])
def cheif_warden(request):
    block_list = blocks.objects.all()
    context = {'block_list': block_list}
    return render(request, 'cheif_warden/starting_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def create_block(request):
    create_block_form = Block_form()
    if request.method == 'POST':
        create_block_form = Block_form(request.POST)
        if create_block_form.is_valid():
            create_block_form.save()
            return redirect('cheif_warden_home')

    context = {'form_table': create_block_form}
    return render(request, 'cheif_warden/create_block_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def create_floor(request):
    create_floor_form = floor_form()
    if request.method == 'POST':
        create_floor_form = floor_form(request.POST)
        if create_floor_form.is_valid():
            create_floor_form.save()
            return redirect('cheif_warden_home')

    context = {'form_table': create_floor_form}
    return render(request, 'cheif_warden/create_floor_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def create_room(request):
    create_room_form = room_form()
    if request.method == 'POST':
        create_room_form = room_form(request.POST)
        if create_room_form.is_valid():
            create_room_form.save()
            return redirect('cheif_warden_home')

    context = {'form_table': create_room_form}
    return render(request, 'cheif_warden/create_room_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def create_warden(request):
    create_warden_form = warden_form()
    if request.method == 'POST':
        create_warden_form = warden_form(request.POST)
        if create_warden_form.is_valid():
            form = create_warden_form.save()
            # form.custom_warden_form()
            print("the form id is", form.id)
            floor_id = create_warden_form.data['Floor_Number']
            # print("The floor id is",floor_id)
            floor_temp = floors.objects.get(id=floor_id)
            room_list = floor_temp.room_set.all()
            print("The room list is", room_list)
            # room_list = floor_temp.room_set.all().order_by('Warden_id').update(Warden_id_id = F(int(form.id)))
            for i in room_list:
                print("The warden id before is", i.Warden_id_id)
                print("the warden id from the form", form.id)
                i.Warden_id_id = int(form.id)
                # warden_name= User.objects.get(id=int(create_warden_form.data['Warden_ID']))
                # i.Warden_id = warden_name
                print("The warden id after is", i.Warden_id_id)
                print("The room is", i)
                # print("The warden name is",warden_name)
                i.save()
            return redirect('cheif_warden_home')

    context = {'form_table': create_warden_form}
    return render(request, 'cheif_warden/create_warden_page.html', context)
