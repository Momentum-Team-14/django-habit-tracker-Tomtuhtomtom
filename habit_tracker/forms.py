from .models import Habit, Record
from django import forms
from django.utils import timezone


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ("name", "target_number", "unit_of_measure")


class RecordForm(forms.ModelForm):
    entry_date = forms.DateField(
        widget=forms.SelectDateWidget(
            empty_label=('Choose Year', 'Choose Month', 'Choose Day')
            ), initial=timezone.now(),
            )

    class Meta:
        model = Record
        fields = ("entry_date", "result")