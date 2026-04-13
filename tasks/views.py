from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Category, Priority, SubTask, Note
from .forms import (
    TaskForm,
    CategoryForm,
    PriorityForm,
    SubTaskForm,
    NoteForm
)

# =========================
# HOME / DASHBOARD
# =========================
@login_required
def home(request):
    context = {
        # Task Status Stats
        'total_tasks': Task.objects.count(),
        'completed_tasks': Task.objects.filter(status='Completed').count(),
        'in_progress_tasks': Task.objects.filter(status='In Progress').count(),
        'pending_tasks': Task.objects.filter(status='Pending').count(),
        
        # General Stats
        'total_categories': Category.objects.count(),
        'total_notes': Note.objects.count(),
        'total_priorities': Priority.objects.count(),
        'total_subtasks': SubTask.objects.count(),
        
        # Recent Tasks Table
        'tasks': Task.objects.all().order_by('-created_at')[:5],
        'page_title': 'Dashboard Overview'
    }
    return render(request, 'home.html', context)

# =========================
# TASKS
# =========================
@login_required
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form, 'title': 'Create Task'})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form, 'title': 'Update Task'})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_del.html', {'task': task})

# Note: Panatilihin ang ibang views (Category, Priority, Subtask, Note) gaya ng dati mong code.
# =========================
# CATEGORY
# =========================
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_del.html', {'category': category})


# =========================
# PRIORITY
# =========================
@login_required
def priority_list(request):
    priorities = Priority.objects.all()
    return render(request, 'priority_list.html', {'priorities': priorities})

@login_required
def priority_create(request):
    form = PriorityForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('priority_list')
    return render(request, 'priority_form.html', {'form': form})

@login_required
def priority_update(request, pk):
    priority = get_object_or_404(Priority, pk=pk)
    form = PriorityForm(request.POST or None, instance=priority)
    if form.is_valid():
        form.save()
        return redirect('priority_list')
    return render(request, 'priority_form.html', {'form': form})

@login_required
def priority_delete(request, pk):
    priority = get_object_or_404(Priority, pk=pk)
    if request.method == 'POST':
        priority.delete()
        return redirect('priority_list')
    return render(request, 'priority_del.html', {'priority': priority})


# =========================
# SUBTASK
# =========================
@login_required
def subtask_list(request):
    subtasks = SubTask.objects.all()
    return render(request, 'subtask_list.html', {'subtasks': subtasks})

@login_required
def subtask_create(request):
    form = SubTaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'subtask_form.html', {'form': form})

@login_required
def subtask_delete(request, pk):
    subtask = get_object_or_404(SubTask, pk=pk)
    if request.method == 'POST':
        subtask.delete()
        return redirect('task_list')
    return render(request, 'subtask_del.html', {'subtask': subtask})


# =========================
# NOTE
# =========================
@login_required
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})

@login_required
def note_create(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('task_list')
    return render(request, 'note_del.html', {'note': note})