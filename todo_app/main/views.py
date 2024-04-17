from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Task
# Create your views here.


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
    completedTasks = Task.objects.filter(is_completed=True)
    context = {'tasks': tasks, 'completedTasks': completedTasks}
    return render(request, 'task.html', context)


def addTask(request):
    newTask = request.POST['task']
    if not newTask:
        return redirect('home')
    Task.objects.create(task=newTask, is_completed=False)
    return redirect('home')


def taskComplete(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def unmarkTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def editTask(request, pk):
    editTask = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        editTask.task = request.POST['task']
        editTask.save()
        return redirect('home')
    else:
        context = {'editTask': editTask}
        return render(request, 'editTask.html', context)


def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
