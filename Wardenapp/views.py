from django.shortcuts import render, redirect
from hostelapp.models import *
from .filters import *
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from accounts.decorators import *
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from accounts.models import CustomUser
from _datetime import datetime, timezone


# Create your views here.

def home(request):
    return render(request, 'Wardenapp/home.html')


@allowed_users(allowed_roles=['warden'])
def blocks_view(request):
    wardenname = warden.objects.filter(Warden_ID=request.user)
    # print(wardenname, request.user)
    context = {'warden': wardenname, 'warden_name': request.user}
    return render(request, 'Wardenapp/blocks.html', context)


'''def floors(request,pk):
    #wardenname=warden.objects.filter(Warden_ID=request.user)
    block_tem = blocks.objects.filter(id=pk)
    floorname=block_tem.floors_set.all()
    context={'floors':floorname}
    return render(request,'Wardenapp/floors.html',context)'''
#@allowed_users(allowed_roles=['warden'])
def issues_view(request):
    issues=issue_raiser.objects.all()
    context={'issues':issues}
    return render(request, 'Wardenapp/issues.html', context)

#@allowed_users(allowed_roles=['warden'])
def issues_detail(request,pk):
    stud= issue_student.objects.filter(issueid_id=pk)

    context={'stud':stud}
    return render(request, 'Wardenapp/issues_det.html', context)


@allowed_users(allowed_roles=['warden'])
def floors_view(request, pk):
    floor_list = floors.objects.filter(id=pk)
    print(floor_list)
    wanden_name = warden.objects.filter(Warden_ID=request.user)
    warden_floor_list = [i.Floor_Number for i in wanden_name]
    check = any(item in warden_floor_list for item in floor_list)
    if check:
        context = {'floor_list': floor_list}
        return render(request, 'Wardenapp/floors.html', context)
    else:
        message = "Page dose not exist or You are not authorized to view this page"
        messages.error(request, message)
        print(message)
        return redirect('default_home_name')


@allowed_users(allowed_roles=['warden'])
def gate_view(request):
    temp = warden.objects.get(Warden_ID_id=request.user.id)
    gate_pass_stud = gatepass.objects.filter(Warden_id_id=temp.id)
    context = {'gatepass_stud': gate_pass_stud}
    return render(request, 'Wardenapp/gate.html', context)


@allowed_users(allowed_roles=['warden'])
def approve_view(request, pk, bi):
    appr = gatepass.objects.filter(user_id=pk)
    for i in appr:
        if str(i.outing_date) == str(bi):
            i.approval_status = True
            i.save()
            message = "Successfully Updated"
            messages.success(request, message)
            break
    return redirect('gate')


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


class update_password(PasswordChangeView):
    form_class = passwordchangingform
    # messages.add_message(self.request, messages.INFO, 'Hello world.')
    success_message = "Your Password was successfully Changed!"
    success_url = reverse_lazy('warden_blocks')


def date_of_attendence(request):
    form = attendence_date_form()
    if request.method == "POST":
        form = attendence_date_form(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('datetaken')
            current_date = datetime.now(timezone.utc)
            diff = date - current_date
            # print("current date",current_date)
            # print("date from form",date)
            #print("$$$$$$$$$$$$$$$$$$$", diff.days, diff.days + 1)
            last_row_check = students_attendence.objects.filter(room_num__Warden_id__Warden_ID=request.user).last()
            filter_check = students_attendence.objects.filter(student_name=last_row_check.student_name,
                                                              date__datetaken__day=date.day,
                                                              room_num__Warden_id__Warden_ID=request.user)
            if len(filter_check) > 1:
                message = "Attendance is taken already "
                messages.error(request, message)
                return redirect('everything_to_attendance')
            if diff.days + 1 < 0:
                #print('&&&&&&&&&&&&&&', diff.days, diff)
                message = "You entered a past date. Please Select today date"
                messages.error(request, message)
                return redirect('attendance_date')
            if diff.days + 1 >= 1:
                #print('&&&&&&&&&&&&&&', diff.days, diff)
                message = "You have choosen the future date. Please select the today date"
                messages.error(request, message)
                return redirect('attendance_date')
            entered_warden = CustomUser.objects.get(username=request.user)
            attendence_date.objects.create(datetaken=date, warden=entered_warden)
            return redirect('everything_to_attendance')
    context = {'form': form}
    return render(request, 'Wardenapp/attendance_date.html', context)


def online_attendence(request):
    today_attend = students_attendence.objects.filter(room_num__Warden_id__Warden_ID=request.user,
                                                      date__datetaken__day=datetime.now().day)
    # form = attendance_form()
    # if request.method == "POST":
    #     form = attendance_form(request.POST)
    #     if form.is_valid():
    #         pass
    #         f_student_name = form.cleaned_data.get('student_name')
    #         f_room_num = form.cleaned_data.get('room_num')
    #         f_date = form.cleaned_data.get('date')
    #         update_attend=form.save(commit=False)
    #         instance = students_attendence.objects.get(student_name=f_student_name, room_num=f_room_num, date=f_date)
    #         instance.present = form.cleaned_data.get('present')
    #         instance.save()
    context = {'attendance_list': today_attend}
    return render(request, 'Wardenapp/attendance_list.html', context)


def save_attendance(request, pk):
    instance = students_attendence.objects.get(id=pk)
    # print("******************",instance)
    if instance.present:
        instance.present = False
    else:
        instance.present = True
    instance.save()
    return redirect('attendance_list')


def everything_to_attendance(request):
    return render(request, 'Wardenapp/everything_to_attendance.html')


def view_attendance(request):
    form = attendence_date_form()
    if request.method == "POST":
        form = attendence_date_form(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('datetaken')
            attended = students_attendence.objects.filter(room_num__Warden_id__Warden_ID=request.user,
                                                          date__datetaken__day=date.day)
            # myfilter = students_attendencefilter(request.GET,queryset=attended)
            # attended = myfilter.qs
            if len(attended) == 0:
                message = "The date you have choosen has no Attendance or Attendance is not taken yet"
                messages.error(request, message)
                return redirect('everything_to_attendance')
            context1 = {'attendance': attended}
            return render(request, 'Wardenapp/view_attendance.html', context1)
    context = {'form': form}
    return render(request, 'Wardenapp/attendance_date.html', context)
