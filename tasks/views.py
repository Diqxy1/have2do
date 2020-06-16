from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
task_list = []


def tasks(request):
    context = {'tasks': task_list}
    return render(request, 'tasks.html', context)

def add_task(request):
    if request.method == 'POST':
        task = Task(request.POST['task'],
                    request.POST['description'],
                    request.POST['image'])
        task_list.append(task)

        return redirect('/tasks/tasks')

    return render(request, 'add_task.html')
