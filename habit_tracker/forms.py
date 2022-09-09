from .models import Habit, Record
from django import forms


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ("name", "target_number", "unit_of_measure")


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ("habit", "entry_date", "result")