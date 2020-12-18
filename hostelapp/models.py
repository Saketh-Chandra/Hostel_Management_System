from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class blocks(models.Model):
    Block_Name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.Block_Name


class floors(models.Model):
    Floor_Number = models.IntegerField(null=True)
    Number_of_Rooms = models.IntegerField(null=True)
    Block_Name = models.ForeignKey(blocks, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(str(self.Floor_Number) + " " + str(self.Block_Name))


class warden(models.Model):
    Warden_ID = models.ForeignKey(User, limit_choices_to={'groups__name': "warden"}, null=True,
                                  on_delete=models.SET_NULL)
    Block_Name = models.ForeignKey(blocks, null=True, on_delete=models.SET_NULL)
    Floor_Number = models.ForeignKey(floors, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.Warden_ID)


class room(models.Model):
    Room_No = models.IntegerField(null=True)
    Floor_Number = models.ForeignKey(floors, null=True, on_delete=models.SET_NULL)
    Block_Name = models.ForeignKey(blocks, null=True, on_delete=models.SET_NULL)
    Capacity = models.IntegerField(default=4)
    # Cost = models.BigIntegerField(null=True)
    Number_already_occupied = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]
    )
    Warden_id = models.ForeignKey(warden, null=True, on_delete=models.CASCADE, blank=True)
    hide = models.BooleanField(default=False)

    # tese_ID = models.ForeignKey(User, limit_choices_to={'groups__name': "warden"}, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(str(self.Room_No) + " " + str(self.Block_Name))


class student_room(models.Model):
    user = models.OneToOneField(User, limit_choices_to={'groups__name': "student"}, on_delete=models.CASCADE,
                                null=False,
                                unique=True)
    # user = models.ForeignKey(User, limit_choices_to={'groups__name': "student"}, on_delete=models.CASCADE, null=False,unique=True)
    user_room = models.ForeignKey(room, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'{self.user} {self.user_room}'
