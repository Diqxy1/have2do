from django.shortcuts import render, redirect

task_list = []


def tasks(request):
    return render(request, 'tasks.html', {'tasks': task_list})

def add_task(request):
    if request.method == 'POST':
        data = {
            'title': request.POST['task'],
            'description': request.POST['description'],
            'image': request.POST['image'],
        }
        task_list.append(data)

        return redirect('/tasks/')

    return render(request, 'add_task.html')
