import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pawpal_system import Pet, Owner, Task


def test_mark_complete_updates_status():
    pet = Pet("Minmin", "Cat", "American Shorthair", 5, "Female")
    task = Task(task_type="vet", pet=pet, date="2026-04-15 11:00 AM", notes="Checkup")
    assert task.status == "pending"
    task.mark_complete()
    assert task.status == "completed"


def test_adding_task_increases_task_count():
    owner = Owner("Mimi")
    pichu = Pet("Pichu", "Cat", "American Shorthair", 1.5, "Male")
    owner.add_pet(pichu)
    assert pichu.task_count == 0
    owner.scheduler.schedule_feeding_time(pichu, "2026-04-01", "every 4 hours")
    assert pichu.task_count == 1
