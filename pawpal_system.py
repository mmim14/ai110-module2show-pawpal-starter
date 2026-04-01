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


class Scheduler:
    def __init__(self, owner):
        self.owner = owner
        self.schedule = {
            "feeding": [],
            "vet": [],
            "grooming": [],
        }

    def schedule_feeding_time(self, pet, time, frequency):
        pass

    def schedule_vet_appointment(self, pet, date, clinic):
        pass

    def schedule_grooming_appointment(self, pet, date, groomer):
        pass

    def _has_conflict(self, pet, date):
        pass
