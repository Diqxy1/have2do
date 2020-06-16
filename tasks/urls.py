from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('add/tasks/', views.add_task, name='add_tasks'),
]
