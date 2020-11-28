from django.db.models import F
from django.shortcuts import render, redirect
from hostelapp.models import *
from .forms import *
from django.conf import settings
from accounts.decorators import *
from django.contrib import messages

User = settings.AUTH_USER_MODEL


# Create your views here.
@allowed_users(allowed_roles=['chief warden'])
def cheif_warden(request):
    block_list = blocks.objects.all()
    if request.method == 'POST':
        Ref_No = request.POST.get('Ref_No')
        print(Ref_No)
        return redirect('update_student_room_name', pk=Ref_No)
    context = {'block_list': block_list}
    return render(request, 'cheif_warden/starting_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def create_block(request):
    create_block_form = Block_form()
    if request.method == 'POST':
        create_block_form = Block_form(request.POST)
        if create_block_form.is_valid():
            create_block_form.save()
            message = "Created Block is successfully done"
            messages.success(request, message)
            return redirect('cheif_warden_home')
        else:
            message = "Created Block is Failed"
            messages.error(request, message)
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
            message = "Created floor is successfully done"
            messages.success(request, message)
            return redirect('cheif_warden_home')
        else:
            message = "Created floor is Failed"
            messages.error(request, message)
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
            message = "Created room is successfully done"
            messages.success(request, message)
            return redirect('cheif_warden_home')
        else:
            message = "Created room is Failed"
            messages.error(request, message)
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
            message = "Successfully warden is created"
            messages.success(request, message)
            return redirect('cheif_warden_home')
        else:
            message = "Failed to created  warden! "
            messages.error(request, message)
            return redirect('cheif_warden_home')
    context = {'form_table': create_warden_form}
    return render(request, 'cheif_warden/create_warden_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def update_student_room(request, pk):
    try:
        student_info_room = student_room.objects.get(id=pk)
        print(student_info_room.user, student_info_room.user_room)
        old_room_data = student_info_room.user_room_id
        student_room_form = update_booking_form(instance=student_info_room)

        if request.method == 'POST':
            new_student_room_form = update_booking_form(request.POST, instance=student_info_room)
            if new_student_room_form.is_valid():
                # student_info_room

                old_room_id = old_room_data
                old_room = room.objects.get(id=old_room_id)
                print(f'old room {old_room}')
                print(f'old room redo {old_room.Number_already_occupied}')
                old_room.Number_already_occupied -= 1
                print(f'old room updated {old_room.Number_already_occupied}')

                new_room_data = new_student_room_form.data['user_room']

                new_room = room.objects.get(id=new_room_data)
                capacity = new_room.Capacity
                occupied = new_room.Number_already_occupied
                print(f'new room {new_room}')
                print(f'ner room redo {new_room.Number_already_occupied}')
                if capacity > occupied:
                    new_room.Number_already_occupied += 1
                    print(f'new room redo {new_room.Number_already_occupied}')
                    new_room.save()
                    new_student_room_form.save()
                    old_room.save()
                    student_room_form = new_student_room_form
                    message = "Successfully Student room update"
                    messages.success(request, message)
                    return redirect('cheif_warden_home')
                else:
                    message = "Room is already occupied"
                    messages.error(request, message)
            else:

                message = "Failed to update Student room"
                messages.error(request, message)
                # print(f'new room {new_room_data} old room {old_room}')

                # student_info_room.room.save()
                # student_save_form = student_room_form.save()
        context = {'student_room_form': student_room_form, 'student_info_room': student_info_room}
        # print(student_room_form, '---')
        return render(request, 'cheif_warden/student_room_update_page.html', context)
    except Exception:
        message = "Student don't created room!!"
        messages.error(request, message)
        return redirect('cheif_warden_home')


@allowed_users(allowed_roles=['chief warden'])
def chief_floors(request, pk):
    chief_block = blocks.objects.get(id=pk)
    chief_floors_list = chief_block.floors_set.all()
    context = {'chief_floors_list': chief_floors_list}
    return render(request, 'cheif_warden/floors.html', context)


@allowed_users(allowed_roles=['chief warden'])
def chief_rooms(request, pk):
    floor_temp = floors.objects.get(id=pk)
    chief_rooms_list = floor_temp.room_set.all()
    context = {'chief_rooms_list': chief_rooms_list}
    return render(request, 'cheif_warden/rooms.html', context)


@allowed_users(allowed_roles=['chief warden'])
def student_view(request, pk):
    student_list = student_room.objects.filter(user_room_id=pk)
    context = {'student_list': student_list}
    print(student_list)
    return render(request, 'cheif_warden/student_info_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def warden_list(request):
    w_list = warden.objects.all()
    context = {'w_list': w_list}
    return render(request, 'cheif_warden/warden_list_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def update_warden(request, pk):
    try:
        warden_info = warden.objects.get(id=pk)
        form_w = update_warden_form(instance=warden_info)
        if request.method == 'POST':
            form_w = update_warden_form(request.POST, instance=warden_info)
            if form_w.is_valid():
                form_w.save()
                message = "Successfully warden room update"
                messages.success(request, message)
                return redirect('cheif_warden_home')
            else:
                message = "warden don't updated room!!"
                messages.error(request, message)
                redirect('cheif_warden_home')

        context = {'form_w': form_w, 'warden_info': warden_info}
        return render(request, 'cheif_warden/update_warden_page.html', context)
    except Exception:
        message = "Warden dose not existed !"
        messages.error(request, message)
        return redirect('cheif_warden_home')
