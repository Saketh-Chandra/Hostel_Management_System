from django.db.models.signals import post_save
from django.dispatch import receiver
from hostelapp.models import attendence_date,student_room,students_attendence


@receiver(post_save,sender=attendence_date)
def get_ready(sender,instance,created,**kwargs):
    if created:
        print("Create the list of students for the day.")
        #lis = student_room.objects.all()
        students = student_room.objects.all().filter(user_room__Warden_id__Warden_ID=instance.warden)
        print("___________", students, "__________________")
        #students = list(students)
        print("___________", students, "__________________")
        for dat in students:
            students_attendence.objects.create(date=instance, student_name=dat.user, room_num=dat.user_room)
        print("The list of students are")
        #print(lis)