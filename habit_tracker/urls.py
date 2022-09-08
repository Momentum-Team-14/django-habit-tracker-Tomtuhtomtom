from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('habits/', views.list_habits, name='list-habits'),
    path('habits/new', views.add_habit, name='add-habit'),
    path('habits/<int:pk>', views.habit_detail, name='habit-detail'),
    path('habits/<int:pk>/edit', views.edit_habit, name='edit-habit'),
    path('habits/<int:pk>/delete', views.delete_habit, name='delete-habit'),
]
