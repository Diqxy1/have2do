from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CategoryForm


# Create your views here.
def category_create(request):
    form = CategoryForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('category_create'))
    return render(request, 'categories/category_create.html', context)
