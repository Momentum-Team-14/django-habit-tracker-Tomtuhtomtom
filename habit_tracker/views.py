from django.shortcuts import render, redirect
from .models import CustomUser, Habit, Record
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("list-habits")
    return render(request, 'index.html', {})


@login_required
def list_habits(request):
    habits = Habit.objects.all().order_by('name')
    return render(request, "habit_tracker/list_habits.html", {"habits": habits})
