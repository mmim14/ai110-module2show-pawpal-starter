from datetime import date
from pawpal_system import Task, Pet, Owner, Scheduler

owner = Owner("Mimi")

minmin = Pet(name="Minmin", species="Cat", breed="American Shorthair", age=5, gender="Female")
pichu  = Pet(name="Pichu",  species="Cat", breed="American Shorthair", age=1.5, gender="Male")
mochi  = Pet(name="Mochi",  species="Cat", breed="Maine Coon", age=.5, gender="Male")

# Task 1: Vet appointment for Minmin on 4/15/2026 at 11 AM
minmin.tasks.append(Task(task_type="vet", pet=minmin, date="2026-04-15 11:00 AM", notes="Clinic visit"))

# Task 2: Feeding for Pichu every 4 hours
pichu.tasks.append(Task(task_type="feeding", pet=pichu, date="2026-04-01", frequency="every 4 hours"))

# Task 3: Grooming appointment for Mochi on 4/21/2026 at 3 PM
mochi.tasks.append(Task(task_type="grooming", pet=mochi, date="2026-04-21 3:00 PM", notes="Grooming session"))

# Print today's schedule
today = str(date.today())
all_pets = [minmin, pichu, mochi]

print(f"--- Today's Schedule ({today}) ---")
for pet in all_pets:
    for task in pet.tasks:
        if task.date.startswith(today):
            print(f"[{task.task_type.upper()}] {pet.name} — {task.date}"
                  + (f" | {task.notes}" if task.notes else "")
                  + (f" | {task.frequency}" if task.frequency else ""))
