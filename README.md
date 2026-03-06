# Hangarin: Task & To-Do Manager

A simple yet powerful web application built with Django that helps users organize daily tasks, manage priorities, add notes, and break down large goals into smaller subtasks. Includes a comprehensive admin interface for easy management and data visualization.

## Features

### Task Management
- **Create and manage tasks** with:
  - Title and description
  - Deadline
  - Status: Pending, In Progress, Completed
  - Priority: High, Medium, Low, Critical, Optional
  - Category: Work, School, Personal, Finance, Projects

### Subtasks & Notes
- Add subtasks to break down larger tasks
- Attach notes to tasks for additional context

### Admin Interface
- Filters and search functionality for tasks, subtasks, and notes
- Custom display fields for better data visualization
- Clean plural naming with verbose_name_plural
- Faker-generated sample data for testing

## Entity Relationship Diagram (ERD)

### Database Schema

| Table | Fields |
|-------|--------|
| **Priority** | id, name |
| **Category** | id, name |
| **Task** | id, title, description, deadline, status, category_id, priority_id |
| **SubTask** | id, parent_task_id, title, status |
| **Note** | id, task_id, content |

### Relationships

```
Priority (1) ──→ (Many) Tasks
Category (1) ──→ (Many) Tasks
Task (1) ──→ (Many) SubTasks
Task (1) ──→ (Many) Notes
```

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/Django_Hangarin.git
cd hangarin
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to access the admin panel.

## Populating Sample Data

Use the built-in Faker script to generate sample tasks, subtasks, and notes for testing:

```bash
python manage.py seed_data
```

This will populate your database with realistic test data.

## Admin Configuration

### TaskAdmin
- **Display Fields**: title, status, deadline, priority, category
- **Filters**: status, priority, category
- **Search**: title and description

### SubTaskAdmin
- **Display Fields**: title, status, parent task
- **Filters**: status
- **Search**: title

### CategoryAdmin & PriorityAdmin
- **Display Fields**: name
- **Search**: searchable by name

### NoteAdmin
- **Display Fields**: task, content, created_at
- **Filters**: created_at
- **Search**: content

## Deployment

Deploy the project on PythonAnywhere:

1. Clone your repository
2. Create a virtual environment and install dependencies
3. Run migrations (`python manage.py migrate`)
4. Configure the web app and WSGI path in PythonAnywhere
5. Reload the web app
6. Access your application via the provided URL

For detailed PythonAnywhere deployment instructions, refer to their [official documentation](https://help.pythonanywhere.com/).

## Technologies Used

- **Python 3.x** - Programming language
- **Django** - Web framework
- **Faker** - Test data generation
- **SQLite** - Default database (can be switched to MySQL/PostgreSQL)

## Project Structure

```
Django_Hangarin/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── hangarin_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── tasks/
    ├── models.py
    ├── views.py
    ├── admin.py
    ├── management/
    │   └── commands/
    │       └── seed_data.py
    └── migrations/
```

## Getting Help

If you encounter any issues, please:

1. Check the Django documentation: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
2. Review the terminal output for error messages
3. Ensure all dependencies are properly installed



## Author

Jonathan Fajiculay
