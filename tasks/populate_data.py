import os
import sys
import django
import random
from faker import Faker
from django.utils import timezone

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)).replace("\\tasks", ""))

# Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hangarin_project.settings')
django.setup()

from tasks.models import Task, SubTask, Note, Category, Priority

fake = Faker()

# Ensure Categories exist
category_names = ["Work", "School", "Personal", "Finance", "Projects"]
for name in category_names:
    Category.objects.get_or_create(name=name)

# Ensure Priorities exist
priority_names = ["High", "Medium", "Low", "Critical", "Optional"]
for name in priority_names:
    Priority.objects.get_or_create(name=name)

categories = list(Category.objects.all())
priorities = list(Priority.objects.all())

# Generate fake tasks
for _ in range(20):
    task = Task.objects.create(
        title=fake.sentence(nb_words=5),
        description=fake.paragraph(nb_sentences=3),
        status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
        deadline=timezone.make_aware(fake.date_time_this_month()),
        priority=random.choice(priorities),
        category=random.choice(categories)
    )

    # Add 1-3 subtasks
    for _ in range(random.randint(1, 3)):
        SubTask.objects.create(
            task=task,
            title=fake.sentence(nb_words=4),
            status=fake.random_element(elements=["Pending", "In Progress", "Completed"])
        )

    # Add 1-2 notes
    for _ in range(random.randint(1, 2)):
        Note.objects.create(
            task=task,
            content=fake.paragraph(nb_sentences=2)
        )

print("Fake data generated successfully!")