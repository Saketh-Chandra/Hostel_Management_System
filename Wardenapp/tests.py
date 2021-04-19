from django.test import TestCase

# Create your tests here.

#Form
class attendence_date_form(forms.Form):
    datetaken = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    class Meta:
        model = attendence_date
        fields = ['datetaken']
        exclude = ['warden']
#URL
path('attendance/date',views.date_of_attendence,name='attendance_date'),

#models
class attendence_date(models.Model):
    warden = models.ForeignKey(User, limit_choices_to={'groups__name': "warden"}, null=True,
                                  on_delete=models.SET_NULL)
    datetaken = models.DateTimeField()

    def __str__(self):
        return str(self.datetaken)

class students_attendence(models.Model):
    student_name = models.ForeignKey(User, limit_choices_to={'groups__name': "student"}, null=True,
                                  on_delete=models.SET_NULL)
    room_num = models.ForeignKey(room,on_delete=models.SET_NULL,null=True)
    date = models.ForeignKey(attendence_date,on_delete=models.SET_NULL,null=True)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student_name} {self.present} {self.date}'

#Views
def date_of_attendence(request):
    form = attendence_date_form()
    if request.method == "POST":
        form = attendence_date_form(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'Wardenapp/attendance_date.html',context)

def online_attendence(request):
    today_attend = students_attendence.objects.filter()

#signal
from django.db.models.signals import post_save
from django.dispatch import receiver
from hostelapp.models import attendence_date,student_room,students_attendence


@receiver(post_save,sender=attendence_date)
def get_ready(sender,instance,created,**kwargs):
    if created:
        print("Create the list of students for the day.")
        #lis = student_room.objects.all()
        students = student_room.objects.all()
        for dat in students:
            students_attendence.objects.create(date=instance, student_name=dat.user, room_num=dat.user_room)
        print("The list of students are")
        #print(lis)