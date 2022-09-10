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

urlpatterns += [
    path('records/', views.list_records, name='list-records'),
    path('habits/<int:pk>/records/new', views.add_record, name='add-record'),
    path('records/<int:pk>', views.record_detail, name='record-detail'),
    path('records/<int:pk>/edit', views.edit_record, name='edit-record'),
    path('records/<int:pk>/delete', views.delete_record, name='delete-record'),
]

# urlpatterns += [
#     path('habits/<int:pk>/<int:year>/<int:month>/<int:day>', views.record_detail, name='record-detail'),
# ]