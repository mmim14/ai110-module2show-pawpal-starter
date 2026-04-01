class Pet:
    def __init__(self, name, species, breed, age, gender, medical_notes=""):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.gender = gender
        self.medical_notes = medical_notes

    def get_info(self):
        pass


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        pass

    def remove_pet(self, pet_name):
        pass

    def get_pets(self):
        pass


class Scheduler:
    def __init__(self):
        self.schedule = []

    def schedule_feeding_time(self, pet, time):
        pass

    def schedule_vet_appointment(self, pet, date, clinic):
        pass

    def schedule_grooming_appointment(self, pet, date, groomer):
        pass
