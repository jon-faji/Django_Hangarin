from django.contrib import admin
from django.urls import path, include

from tasks.views import (
    HomePageView,
    PriorityListView, PriorityCreateView, PriorityUpdateView, PriorityDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView,
    SubTaskListView, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView,
    OrganizationListView, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
)

urlpatterns = [
    # =========================
    # ADMIN
    # =========================
    path('admin/', admin.site.urls),

    # =========================
    # AUTH (ALLAUTH)
    # =========================
    path('accounts/', include('allauth.urls')),

    # =========================
    # MAIN DASHBOARD
    # =========================
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', HomePageView.as_view(), name='dashboard'),

    # =========================
    # PRIORITY
    # =========================
    path('priority_list/', PriorityListView.as_view(), name='priority-list'),
    path('priority_list/add/', PriorityCreateView.as_view(), name='priority-add'),
    path('priority_list/<pk>/', PriorityUpdateView.as_view(), name='priority-update'),
    path('priority_list/<pk>/delete/', PriorityDeleteView.as_view(), name='priority-delete'),

    # =========================
    # CATEGORY
    # =========================
    path('category_list/', CategoryListView.as_view(), name='category-list'),
    path('category_list/add/', CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category_list/<pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    # =========================
    # TASK
    # =========================
    path('task_list/', TaskListView.as_view(), name='task-list'),
    path('task_list/add/', TaskCreateView.as_view(), name='task-add'),
    path('task_list/<pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    # =========================
    # NOTE
    # =========================
    path('note_list/', NoteListView.as_view(), name='note-list'),
    path('note_list/add/', NoteCreateView.as_view(), name='note-add'),
    path('note_list/<pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('note_list/<pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),

    # =========================
    # SUBTASK
    # =========================
    path('subtask_list/', SubTaskListView.as_view(), name='subtask-list'),
    path('subtask_list/add/', SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtask_list/<pk>/', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtask_list/<pk>/delete/', SubTaskDeleteView.as_view(), name='subtask-delete'),

    # =========================
    # ORGANIZATION
    # =========================
    path('organization_list/', OrganizationListView.as_view(), name='organization-list'),
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),
]