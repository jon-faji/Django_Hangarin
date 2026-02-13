# Hangarin: Task & To-Do Manager

## Short Description
Hangarin is a Django-based web application designed to help users organize daily tasks, manage priorities, add notes, and break down large goals into smaller subtasks. It provides a simple yet effective interface for personal and professional task management.

## Features
- **Task Management:** Create, update, and track tasks with status, priority, and category.
- **Subtasks:** Break down tasks into smaller actionable items for better progress tracking.
- **Notes:** Attach notes to tasks to provide additional context or reminders.
- **Priorities & Categories:** Predefined priorities (High, Medium, Low, Critical, Optional) and categories (Work, School, Personal, Finance, Projects).
- **Admin Interface:** Efficiently manage tasks, subtasks, notes, priorities, and categories through Django Admin with search and filter capabilities.
- **Data Population Script:** Generate sample tasks, subtasks, and notes using the Faker library for testing or demo purposes.

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Django_Hangarin
```

### 2. Create a virtual environment
```bash
python -m venv psusenv
psusenv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install django faker
```

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser
```bash
python manage.py createsuperuser
```

### 6. Populate sample data
```bash
python tasks\populate_data.py
```

### 7. Admin Access

Access the Django admin panel at:
```
http://127.0.0.1:8000/admin/
```

Manage tasks, subtasks, notes, categories, and priorities with search and filter options.

## Authors

- Jon Faji
- jasperOlpos27
