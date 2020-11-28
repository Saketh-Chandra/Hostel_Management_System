from django.http import HttpResponse
from django.shortcuts import redirect
from hostelapp.models import student_room
from django.contrib import messages

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('default_home_name')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def is_student_booked(view_func):
    def wrapper_func(request, *args, **kwargs):
        student = student_room.objects.filter(user=request.user)
        if len(student) > 0:
            message = "You already Booked the Room One can Book Only one Room"
            messages.error(request, message)
            return redirect('default_home_name')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                message = "You are not authorized to view this page"
                messages.success(request, message)
                return redirect('default_home_name')
                # return HttpResponse('')

        return wrapper_func

    return decorator




# def student_wanden_cheif_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#
#         if group == 'student':
#             return redirect('home')
#
#         if group == 'wanden':
#             return redirect('home')
#             # return view_func(request, *args, **kwargs)
#         if group == 'chief warden':
#             return redirect('cheif_warden_home')
#
#     return wrapper_function
