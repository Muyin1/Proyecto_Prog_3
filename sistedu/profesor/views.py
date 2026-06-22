from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesor
from .forms import ProfesorForm

def profesor_list(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor/profesor_list.html', {'profesores': profesores})

def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm()
    return render(request, 'profesor/profesor_form.html', {'form': form, 'titulo_pagina': 'Crear Profesor'})

def profesor_update(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'profesor/profesor_form.html', {'form': form, 'titulo_pagina': 'Editar Profesor'})

def profesor_delete(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('profesor_list')
    return render(request, 'profesor/profesor_confirm_delete.html', {'profesor': profesor})


