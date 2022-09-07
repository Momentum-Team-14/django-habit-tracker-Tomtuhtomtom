from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Habit(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=100, help_text="Enter a name for the habit you'd like to build")
    date_created = models.DateTimeField(auto_now_add=True)
    target_number = models.IntegerField(help_text="Enter target amount per day for Habit")
    unit_of_measure = models.CharField(max_length=20, help_text="Enter unit of measure for target")

    def __str__(self):
        return self.name


class Record(models.Model):
    habit = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='records')
    entry_date = models.DateField()
    result = models.IntegerField(help_text="Enter amount completed")

    def __str__(self):
        return self.result
