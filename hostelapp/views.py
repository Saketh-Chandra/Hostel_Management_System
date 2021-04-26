from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from accounts.decorators import *
import datetime


# Create your views here.
@allowed_users(allowed_roles=['student'])
def home_view_student(request):
    info = student_room.objects.filter(user=request.user)
    context = {'data_info': info}
    # for i in info:
    #     print(i.user_room_id,i.id)
    print(not info)
    return render(request, 'hostelapp/home.html', context=context)


@allowed_users(allowed_roles=['student'])
def raise_issue_view(request):
    issues=issue_raiser.objects.all()
    

    # for iss in issues:
    #     issue_student.objects.create(
    #         issueid=iss.id,
    #         upvote=False,
    #         downvote=False,
    #         user=request.user
    #     )
    stud=issue_student.objects.filter(user=request.user)

    context={'issues':issues,'stud':stud}
    return render(request, 'hostelapp/issues.html', context=context)


def issue_raisers_view(request):
    form=IssueRaiserForm()


    if request.method=='POST':
        form=IssueRaiserForm(request.POST)
        if form.is_valid():
            confirm=form.save(commit=False)
            confirm.user=request.user
            confirm.save()
            message = 'You have successfully raise an issue'
            messages.success(request, message)
            print(message)
            return redirect('home')
        else:
            message = "Fill the form Properly"
            messages.error(request, message)
            return redirect('issueraise')

    context={'form':form}
    return render(request, 'hostelapp/issue_raiserform.html', context=context)

def upvote_view(request,pk):
    
    # issue1=issue_student.objects.get(id=pk)
    k=0
    stud=issue_student.objects.filter(user=request.user)
    if stud.first():
        for i in stud:
            if str(i.issueid_id)==str(pk):
                # issue_raised=issue_student.objects.get(issueid_id=pk)
                # issue_raised.upvote=True
                # issue_raised.downvote=False
                k=0
                i.upvote=True
                i.downvote=False
                i.save()
                # issue_raised.save()
                break
            else: 
                k=1 
    if (not stud.first()) or k==1:
        confirmation=issue_student()
        confirmation.issueid_id=pk
        confirmation.upvote=True
        confirmation.user=request.user
        confirmation.save()

    
    context={}
    message = 'You have Upvoted Successfully'
    messages.success(request, message)
    return redirect('home')

def downvote_view(request,pk):
    context={}
    k=0
    stud=issue_student.objects.filter(user=request.user)
    if stud.first():
        for i in stud:
            if str(i.issueid_id)==str(pk):
                # issue_raised=issue_student.objects.get(issueid_id=pk)
                #issue_raised.upvote=False
               # issue_raised.downvote=True

                i.upvote=False
                i.downvote=True
                k=0
                i.save()
                #issue_raised.save()
                break
            else: 
                k=1 
    if (not stud.first()) or k==1:
        confirmation=issue_student()
        confirmation.issueid_id=pk
        confirmation.downvote=True
        confirmation.user=request.user
        confirmation.save()
    message = 'You have Downvoted Successfully'
    messages.success(request, message)
    return redirect('home')

@allowed_users(allowed_roles=['student'])
@is_student_booked
def block_views(request):
    print(request.user.groups.all()[0])
    blocks_list = blocks.objects.all()
    context = {'blocks_list': blocks_list}
    return render(request, 'hostelapp/block_page.html', context=context)


@allowed_users(allowed_roles=['student'])
def gatepass_state(request):
    gatepass_history = gatepass.objects.filter(user=request.user)
    context = {'history': gatepass_history}
    return render(request, 'hostelapp/gatepass_student_status.html', context)


@allowed_users(allowed_roles=['student'])
def gatepass_view(request):
    form_k = GatepassForm()
    # dates=datetime.date.today()
    # datestr=dates.strftime('%Y-%m-%d')
    # present_month=int(datestr[5]+datestr[6])
    outingdates = gatepass.objects.filter(user=request.user)

    if request.method == 'POST':

        # form_k=GatepassForm(request.POST,instance=stud)
        # form_k.user=request.user
        form_k = GatepassForm(request.POST)
        if (form_k.is_valid()):
            confirm = form_k.save(commit=False)
            confirm.user = request.user
            confirm.approval_status = False
            stu_room = student_room.objects.get(user=request.user).user_room.id
            room_gets = room.objects.get(id=stu_room)
            stu_warden = room_gets.Warden_id_id
            stud_warden = stu_warden
            confirm.Warden_id_id = stud_warden
            # stu_room=student_room.objects.get(user=request.user).user_room
            # room_gets=room.objects.get(Room_No=stu_room)
            # stu_warden=room_gets.Warden_id
            # print("final "+str(stu_warden))
            formout_date_str = form_k.cleaned_data['outing_date']
            temp_date = formout_date_str.strftime('%Y-%m-%d')
            formout_date_int = int(temp_date[5] + temp_date[6])
            count = 0
            for outing in outingdates:
                temp_date = outing.outing_date.strftime('%Y-%m-%d')
                tempint_date = int(temp_date[5] + temp_date[6])
                if (formout_date_int == tempint_date):
                    count += 1
            # print("count= "+str(count))
            if (count >= 2):
                message = "You already have 2 Gatepass for this month. Try again Next Month"
                messages.error(request, message)
                print(message)
                return redirect('home')
            else:

                confirm.save()
                # print(form_k)
                message = 'Your Gatepass is Confirmed'
                messages.success(request, message)
                print(message)
                return redirect('home')
        else:
            message = "Fill the form Properly"
            messages.error(request, message)
            # print(message)
            # url = 'rooms/floor_id/'
            return redirect('home')

    context = {'form': form_k}
    return render(request, 'hostelapp/gatepass_form.html', context)


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
