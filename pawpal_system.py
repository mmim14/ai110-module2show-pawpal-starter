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
        pass

    def get_summary(self):
        pass


class Pet:
    def __init__(self, name, species, breed, age, gender, medical_notes=""):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.gender = gender
        self.medical_notes = medical_notes
        self.owner = None
        self.tasks = []  # tasks belonging to this pet

    def get_info(self):
        pass


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []
        self.scheduler = Scheduler(self)

    def add_pet(self, pet):
        pass

    def get_pets(self):
        pass

    def get_all_tasks(self):
        pass  # aggregates tasks across all owned pets


class Scheduler:
    def __init__(self, owner):
        self.owner = owner  # queries tasks through owner -> pets -> tasks

    def get_tasks_by_type(self, task_type):
        pass  # searches across all owner's pets for matching task_type

    def schedule_feeding_time(self, pet, time, frequency):
        pass  # creates a Task and appends to pet.tasks

    def schedule_vet_appointment(self, pet, date, clinic):
        pass  # creates a Task and appends to pet.tasks

    def schedule_grooming_appointment(self, pet, date, groomer):
        pass  # creates a Task and appends to pet.tasks

    def _has_conflict(self, pet, date):
        pass  # checks pet.tasks for date conflicts
