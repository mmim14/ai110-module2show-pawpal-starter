class Pet:
    def __init__(self, name, species, breed, age, gender, medical_notes=""):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.gender = gender
        self.medical_notes = medical_notes
        self.owner = None

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


class Scheduler:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []  # flat list of Task objects; filter by task.task_type as needed

    def get_tasks_by_type(self, task_type):
        pass

    def schedule_feeding_time(self, pet, time, frequency):
        pass

    def schedule_vet_appointment(self, pet, date, clinic):
        pass

    def schedule_grooming_appointment(self, pet, date, groomer):
        pass

    def _has_conflict(self, pet, date):
        pass
