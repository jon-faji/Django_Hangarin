from django.core.management.base import BaseCommand
from faker import Faker
from tasks.models import Task, SubTask, Note, Priority, Category
from django.utils import timezone
import random

fake = Faker()

class Command(BaseCommand):

    help = "Seed the database with fake tasks, subtasks, and notes"

    def handle(self, *args, **kwargs):

        
        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        
        if not priorities or not categories:
            self.stdout.write(self.style.ERROR(
                "Please add Priority and Category records in admin first."
            ))
            return

        
        SubTask.objects.all().delete()
        Note.objects.all().delete()
        Task.objects.all().delete()
        self.stdout.write(self.style.WARNING("Old tasks, subtasks, and notes cleared."))

        
        for _ in range(20):

            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(
                    elements=["Pending", "In Progress", "Completed"]
                ),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                priority=random.choice(priorities),
                category=random.choice(categories)
            )

            
            for _ in range(3):
                SubTask.objects.create(
                    task=task,  
                    title=fake.sentence(),
                    status=fake.random_element(
                        elements=["Pending", "In Progress", "Completed"]
                    ),
                )

            
            Note.objects.create(
                task=task,
                content=fake.paragraph()
            )

        self.stdout.write(self.style.SUCCESS("Fake data generated successfully!"))