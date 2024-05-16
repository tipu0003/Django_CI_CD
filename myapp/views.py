from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MyModel
from .forms import MyModelForm

def index(request):
    objects = MyModel.objects.all()
    return render(request, 'myapp/index.html', {'objects': objects})

def detail(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    return render(request, 'myapp/detail.html', {'object': obj})

def create(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    else:
        form = MyModelForm()
    return render(request, 'myapp/form.html', {'form': form})

def update(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        form = MyModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('myapp:detail', pk=obj.pk)
    else:
        form = MyModelForm(instance=obj)
    return render(request, 'myapp/form.html', {'form': form})

def delete(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('myapp:index')
    return render(request, 'myapp/confirm_delete.html', {'object': obj})
