from django.db import models


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
    Warden_ID = models.CharField(max_length=20, null=True)
    Block_Name = models.ForeignKey(blocks, null=True, on_delete=models.SET_NULL)
    Floor_Number = models.ForeignKey(floors, null=True, on_delete=models.SET_NULL)
    Name = models.CharField(max_length=20, null=True)
    Gender = models.CharField(max_length=6, null=True)
    DOB = models.DateField(null=True)
    Phone_Number = models.BigIntegerField(null=True)

    def __str__(self):
        return self.Warden_ID


class room(models.Model):
    Room_No = models.IntegerField(null=True)
    Floor_Number = models.ForeignKey(floors, null=True, on_delete=models.SET_NULL)
    Block_Name = models.ForeignKey(blocks, null=True, on_delete=models.SET_NULL)
    Capacity = models.IntegerField(null=True)
    Cost = models.BigIntegerField(null=True)
    Number_already_occupied = models.IntegerField(null=True)
    Warden_ID = models.ForeignKey(warden, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return str(str(self.Room_No) + " " + str(self.Block_Name))


class student(models.Model):
    Reg_No = models.CharField(max_length=20, null=True)
    Room_No = models.ForeignKey(room, null=True, on_delete=models.SET_NULL)
    Name = models.CharField(max_length=20, null=True)
    Phone_Number = models.BigIntegerField(null=True)
    DOB = models.DateField(null=True)
    Gender = models.ForeignKey(blocks, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.Reg_No)
