from django.shortcuts import render, redirect

task_list = []
description_list = []
image_list = []


def tasks(request):
    return render(request, 'tasks.html', {'tasks': task_list, 'descriptions': description_list, 'images': image_list})

def add_task(request):
    if request.method == 'POST':
        task_list.append(request.POST['task'])
        description_list.append(request.POST['description'])
        image_list.append(request.POST['image'])
        return redirect('/tasks/')

    return render(request, 'add_task.html')
