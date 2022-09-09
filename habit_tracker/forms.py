from .models import Habit, Record
from django import forms


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ("name", "target_number", "unit_of_measure")


class RecordForm(forms.ModelForm):
    entry_date = forms.DateField(
        widget=forms.SelectDateWidget(
            empty_label=('Choose Year', 'Choose Month', 'Choose Day')
            )
            )

    class Meta:
        model = Record
        fields = ("entry_date", "result")