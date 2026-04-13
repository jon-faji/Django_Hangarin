from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category, Priority, SubTask, Note
from .forms import (
    TaskForm,
    CategoryForm,
    PriorityForm,
    SubTaskForm,
    NoteForm
)

# =========================
# HOME
# =========================
def home(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'tasks': tasks})


# =========================
# TASKS
# =========================
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})


def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_del.html', {'task': task})


# =========================
# CATEGORY
# =========================
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category_form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_del.html', {'category': category})


# =========================
# PRIORITY
# =========================
def priority_list(request):
    priorities = Priority.objects.all()
    return render(request, 'priority_list.html', {'priorities': priorities})


def priority_create(request):
    form = PriorityForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('priority_list')
    return render(request, 'priority_form.html', {'form': form})


def priority_delete(request, pk):
    priority = get_object_or_404(Priority, pk=pk)
    if request.method == 'POST':
        priority.delete()
        return redirect('priority_list')
    return render(request, 'priority_del.html', {'priority': priority})


def priority_update(request, pk):
    priority = get_object_or_404(Priority, pk=pk)

    form = PriorityForm(request.POST or None, instance=priority)

    if form.is_valid():
        form.save()
        return redirect('priority_list')

    return render(request, 'priority_form.html', {'form': form})


# =========================
# SUBTASK
# =========================
def subtask_list(request):
    subtasks = SubTask.objects.all()
    return render(request, 'subtask_list.html', {'subtasks': subtasks})


def subtask_create(request):
    form = SubTaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'subtask_form.html', {'form': form})


def subtask_delete(request, pk):
    subtask = get_object_or_404(SubTask, pk=pk)
    if request.method == 'POST':
        subtask.delete()
        return redirect('task_list')
    return render(request, 'subtask_del.html', {'subtask': subtask})


# =========================
# NOTE
# =========================
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})


def note_create(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'note_form.html', {'form': form})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('task_list')
    return render(request, 'note_del.html', {'note': note})