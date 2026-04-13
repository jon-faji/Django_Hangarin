from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin  # ✅ ADDED

from tasks.models import Task, Organization, Priority, Category, Note, SubTask
from tasks.forms import (
    OrganizationForm,
    PriorityForm,
    TaskForm,
    CategoryForm,
    NoteForm,
    SubTaskForm
)


class PrivateView(LoginRequiredMixin):
    login_url = '/accounts/login/'


# =========================
# HOME PAGE
# =========================
class HomePageView(PrivateView, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'home.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_tasks'] = Task.objects.count()
        context['completed_tasks'] = Task.objects.filter(status='Completed').count()
        context['in_progress_tasks'] = Task.objects.filter(status='In Progress').count()
        context['pending_tasks'] = Task.objects.filter(status='Pending').count()
        context['total_priorities'] = Priority.objects.count()
        context['total_categories'] = Category.objects.count()
        context['total_notes'] = Note.objects.count()
        context['total_subtasks'] = SubTask.objects.count()
        return context


# =========================
# PRIORITY
# =========================
class PriorityListView(PrivateView, ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = 'priority_list.html'
    paginate_by = 10
    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(name__icontains=query))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class PriorityCreateView(PrivateView, CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')


class PriorityUpdateView(PrivateView, UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')


class PriorityDeleteView(PrivateView, DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')


# =========================
# CATEGORY
# =========================
class CategoryListView(PrivateView, ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_list.html'
    paginate_by = 10
    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(name__icontains=query))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class CategoryCreateView(PrivateView, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(PrivateView, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(PrivateView, DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')


# =========================
# TASK
# =========================
class TaskListView(PrivateView, ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort_by', 'title')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )

        if sort_by in ['title', 'status', 'deadline', '-deadline']:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by('title')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['sort_by'] = self.request.GET.get('sort_by', 'title')
        return context


class TaskCreateView(PrivateView, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')


class TaskUpdateView(PrivateView, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')


class TaskDeleteView(PrivateView, DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')


# =========================
# NOTE
# =========================
class NoteListView(PrivateView, ListView):
    model = Note
    context_object_name = 'note'
    template_name = 'note_list.html'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(task__title__icontains=query)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class NoteCreateView(PrivateView, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')


class NoteUpdateView(PrivateView, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')


class NoteDeleteView(PrivateView, DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')


# =========================
# SUBTASK
# =========================
class SubTaskListView(PrivateView, ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = 'subtask_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort_by', 'title')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(task__title__icontains=query)
            )

        if sort_by in ['title', 'status', 'task__title']:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by('title')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['sort_by'] = self.request.GET.get('sort_by', 'title')
        return context


class SubTaskCreateView(PrivateView, CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')


class SubTaskUpdateView(PrivateView, UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')


class SubTaskDeleteView(PrivateView, DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')


# =========================
# ORGANIZATION
# =========================
class OrganizationListView(PrivateView, ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(college__icontains=query)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class OrganizationCreateView(PrivateView, CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')


class OrganizationUpdateView(PrivateView, UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')


class OrganizationDeleteView(PrivateView, DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')