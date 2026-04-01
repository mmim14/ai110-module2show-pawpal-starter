VALID_TASK_TYPES = {"feeding", "vet", "grooming"}


class Task:
    def __init__(self, task_type, pet, date, notes="", status="pending", frequency=None):
        if task_type not in VALID_TASK_TYPES:
            raise ValueError(f"task_type must be one of {VALID_TASK_TYPES}")
        self.task_type = task_type
        self.pet = pet
        self.date = date
        self.notes = notes
        self.status = status
        self.frequency = frequency  # only relevant for feeding tasks

    def mark_complete(self):
        self.status = "completed"
        print(f"[{self.task_type.upper()}] {self.pet.name} | {self.date} — marked as completed")

    def get_summary(self):
        return (
            f"[{self.task_type.upper()}] {self.pet.name} | {self.date}"
            + (f" | {self.notes}" if self.notes else "")
            + (f" | {self.frequency}" if self.frequency else "")
            + f" | Status: {self.status}"
        )


class Pet:
    def __init__(self, name, species, breed, age, gender, medical_notes=""):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = float(age)
        self.gender = gender
        self.medical_notes = medical_notes
        self.owner = None
        self.tasks = []  # tasks belonging to this pet

    def get_info(self):
        owner_name = self.owner.name if self.owner else "Unknown"
        return (
            f"Name: {self.name} | Species: {self.species} | Breed: {self.breed} | "
            f"Age: {self.age} yrs | Gender: {self.gender} | Owner: {owner_name}"
            + (f" | Notes: {self.medical_notes}" if self.medical_notes else "")
        )


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []
        self.scheduler = Scheduler(self)

    def add_pet(self, pet):
        pet.owner = self
        self.pets.append(pet)

    def get_pets(self):
        for pet in self.pets:
            print(pet.get_info())

    def get_all_tasks(self):
        for pet in self.pets:
            for task in pet.tasks:
                print(f"[{task.task_type.upper()}] {pet.name} | {task.date}"
                      + (f" | {task.notes}" if task.notes else "")
                      + (f" | {task.frequency}" if task.frequency else "")
                      + f" | Status: {task.status}")


class Scheduler:
    def __init__(self, owner):
        self.owner = owner  # queries tasks through owner -> pets -> tasks

    def get_tasks_by_type(self, task_type):
        matches = [
            task
            for pet in self.owner.pets
            for task in pet.tasks
            if task.task_type == task_type
        ]
        for task in matches:
            print(f"[{task.task_type.upper()}] {task.pet.name} | {task.date}"
                  + (f" | {task.notes}" if task.notes else "")
                  + (f" | {task.frequency}" if task.frequency else "")
                  + f" | Status: {task.status}")

    def schedule_feeding_time(self, pet, time, frequency):
        task = Task(task_type="feeding", pet=pet, date=time, frequency=frequency)
        pet.tasks.append(task)
        print(f"Scheduled: [FEEDING] {pet.name} | {time} | {frequency}")

    def schedule_vet_appointment(self, pet, date, clinic):
        if self._has_conflict(pet, date):
            print(f"Conflict: {pet.name} already has a task on {date}")
            return
        task = Task(task_type="vet", pet=pet, date=date, notes=clinic)
        pet.tasks.append(task)
        print(f"Scheduled: [VET] {pet.name} | {date} | {clinic}")

    def schedule_grooming_appointment(self, pet, date, groomer):
        if self._has_conflict(pet, date):
            print(f"Conflict: {pet.name} already has a task on {date}")
            return
        task = Task(task_type="grooming", pet=pet, date=date, notes=groomer)
        pet.tasks.append(task)
        print(f"Scheduled: [GROOMING] {pet.name} | {date} | {groomer}")

    def _has_conflict(self, pet, date):
        return any(task.date == date for task in pet.tasks)
