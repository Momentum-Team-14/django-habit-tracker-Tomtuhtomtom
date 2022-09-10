from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, Habit, Record
from django.contrib.auth.decorators import login_required
from .forms import HabitForm, RecordForm
from django.db.models import Avg
import datetime

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("list-habits")
    return render(request, 'index.html', {})


@login_required
def list_habits(request):
    habits = Habit.objects.filter(user=request.user).order_by('name')
    return render(request, "habit_tracker/list_habits.html", {"habits": habits})


@login_required
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    records = Record.objects.filter(habit=pk).order_by('-entry_date')
    average = Record.objects.filter(habit=pk).aggregate(Avg('result'))
    return render(
        request,
        'habit_tracker/habit_detail.html',
        {
            "habit": habit,
            "target_number": habit.target_number,
            "unit_of_measure": habit.unit_of_measure,
            "records": records,
            "average": average,
        },
    )


@login_required
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()

            return redirect("list-habits")
    else:
        form = HabitForm()

    return render(request, "habit_tracker/add_habit.html", {"form": form})


@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect("list-habits")
        else:
            print(form.errors)

    return render(request, "habit_tracker/edit_habit.html", {"form": form, "habit": habit})


@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == "POST":
        habit.delete()
        return redirect('list-habits')

    return render(request, 'habit_tracker/delete_habit.html', {"habit": habit})


@login_required
def list_records(request):
    records = Record.objects.filter(habit__user=request.user).order_by('entry_date')
    return render(request, "habit_tracker/list_records.html", {"records": records})


@login_required
def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(
        request,
        'habit_tracker/record_detail.html',
        {
            "record": record,
            "entry_date": record.entry_date,
            "result": record.result,
        },
    )


# @login_required
# def record_detail(request, pk, year=None, month=None, day=None):
#     record = get_object_or_404(Record, pk=pk)
#     if year is None:
#         date_for_record = datetime.date.today()
#     else:
#         date_for_record = datetime.date(year, month, day)
#     next_day = date_for_record + datetime.timedelta(days=1)
#     prev_day = date_for_record + datetime.timedelta(day=-1)

#     record_entry, _ = request.user.record_entries.get_or_create(date=date_for_record)

#     return render(
#         request,
#         'habit_tracker/record_detail.html',
#         {
#             "record": record,
#             "entry_date": record.entry_date,
#             "result": record.result,
#             "date_for_record": date_for_record,
#             "next_day": next_day,
#             "prev_day": prev_day,
#         },
#     )


@login_required
def add_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.habit = habit
            record.save()
            
            return redirect("list-habits")
    else:
        form = RecordForm()

    return render(request, "habit_tracker/add_record.html", {"form": form})


@login_required
def edit_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "GET":
        form = RecordForm(instance=record)
    else:
        form = RecordForm(data=request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("list-records")
        else:
            print(form.errors)

    return render(request, "habit_tracker/edit_record.html", {"form": form, "record": record})


@login_required
def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)

    if request.method == "POST":
        record.delete()
        return redirect('list-records')

    return render(request, 'habit_tracker/delete_record.html', {"record": record})
