from django.shortcuts import render,redirect
from hostelapp.models import *
from .forms import *


# Create your views here.
def cheif_warden(request):
    block_list = blocks.objects.all()
    context = {'block_list':block_list}
    return render(request,'cheif_warden/starting_page.html',context)

def create_block(request):
    create_block_form = Block_form()
    if request.method == 'POST':
        create_block_form = Block_form(request.POST)
        if create_block_form.is_valid():
            create_block_form.save()
            return redirect('cheif_warden_home')

    context = {'form_table': create_block_form}
    return render(request,'cheif_warden/create_block_page.html',context)

def create_floor(request):
    create_floor_form = floor_form()
    if request.method == 'POST':
        create_floor_form = floor_form(request.POST)
        if create_floor_form.is_valid():
            create_floor_form.save()
            return redirect('cheif_warden_home')

    context = {'form_table': create_floor_form}
    return render(request, 'cheif_warden/create_floor_page.html', context)

def create_room(request):
    create_room_form = room_form()
    if request.method == 'POST':
        create_room_form = room_form(request.POST)
        if create_room_form.is_valid():
            create_room_form.save()
            return redirect('cheif_warden_home')

    context = {'form_table': create_room_form}
    return render(request, 'cheif_warden/create_room_page.html', context)

def create_warden(request):
    create_warden_form = warden_form()
    if request.method == 'POST':
        create_warden_form = warden_form(request.POST)
        if create_warden_form.is_valid():
            create_warden_form.save()
            floor_id = create_warden_form.data['Floor_Number']
            #print("The floor id is",floor_id)
            floor_temp = floors.objects.get(id=floor_id)
            room_list = floor_temp.room_set.all()
            for i in room_list:
                print("The warden id is",i.Warden_ID_id)
                print("the warden id from the form",create_warden_form.data['Warden_ID'])
                i.Warden_ID_id = create_warden_form.data['Warden_ID']
                i.save()
                print("The warden id after is", i.Warden_ID_id)
                print("The room is", i)
            return redirect('cheif_warden_home')

    context = {'form_table': create_warden_form}
    return render(request, 'cheif_warden/create_warden_page.html', context)


