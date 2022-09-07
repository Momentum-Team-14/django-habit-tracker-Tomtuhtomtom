from .models import Habit
from django import forms


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ("user", "name", "target_number", "unit_of_measure")
