from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Project

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/project_list.html', context)

def project_create(request):
    if request.method == 'POST':
        title_data = request.POST['title']
        description_data = request.POST['description']
        color_data = request.POST['color']
        Project.objects.create(
        name=title_data,
        description=description_data,
        color=color_data
        )
        return redirect(reverse_lazy('project_list'))
    return render(request, 'projects/project_create.html')
