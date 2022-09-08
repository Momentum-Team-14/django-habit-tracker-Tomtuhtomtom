from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, Habit, Record
from django.contrib.auth.decorators import login_required
from .forms import HabitForm

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
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(
        request,
        'habit_tracker/habit_detail.html',
        {
            "habit": habit,
            "target_number": habit.target_number,
            "unit_of_measure": habit.unit_of_measure,
        },
    )


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
