from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from projects.models import Project
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'tasks/task_list.html', context)


def task_create(request):
    # projects = Project.objects.all()
    form = TaskForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('task_list'))
        # project_id = request.POST['project']
        # title_data = request.POST['title']
        # description_data = request.POST['description']
        # Task.objects.create(
        #     title=title_data,
        #     description=description_data,
        #     project_id=project_id
        # )
    return render(request, 'tasks/task_create.html', context)


def task_detail(request, id):
    task = Task.objects.get(id=id)
    context = {'task':task}
    return render(request, 'tasks/task_detail.html', context)


def task_update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('task_list'))
        # new_title = request.POST['title']
        # new_description = request.POST['description']
        # task.title = new_title
        # task.description = new_description
        # task.save()
    return render(request, 'tasks/task_update.html', context)


def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect(reverse_lazy('task_list'))
