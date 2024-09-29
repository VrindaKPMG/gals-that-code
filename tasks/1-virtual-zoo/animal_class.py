import csv

# Part 1


class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age


# Part 2
class Zoo:
    def __init__(self, opening_time, closing_time):
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(animal.name + " has been added to the zoo")

    def get_all_animals(self):
        for animal in self.animals:
            print(animal.name)

    def get_species_count(self):
        species_count = {}
        for animal in self.animals:
            if animal.species not in species_count:
                species_count[animal.species] = 1
            else:
                species_count[animal.species] += 1
        print(species_count)


# mylion = Lion("Lion", "Simba", 3)
# myelephant = Elephant("Elephant", "Dumbo", 5)
# mylion2 = Lion("Lion", "Mufasa", 4)

myzoo = Zoo("08:00", "18:00")
# myzoo.add_animal(mylion)
# myzoo.add_animal(mylion2)
# myzoo.add_animal(myelephant)
# myzoo.get_species_count()
# myzoo.get_all_animals()


# Part 3

def create_zoo(file_path, zoo_name):

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_animal = Animal(row["species"], row["name"], row["age"])
            zoo_name.add_animal(new_animal)


create_zoo(
    "/Users/vgera1/Desktop/gals-that-code/tasks/1-virtual-zoo/animal.csv", myzoo)


# Part 4

# Time check
def am_I_on_time():
    time = input(
        "When did you arrive at the zoo?\n Please used 24 hour format: ")
    if time > myzoo.closing_time:
        print("The zoo is now closed. You can either go home and come back tomorrow or we have space for one in the lion's cage...")
    if time < myzoo.opening_time:
        print("The zoo is not yet open. Grab a coffee from our neighbours next door (the Costa and not the paint store)")
    else:
        print("You are just in time Enjoy your time!!!")

am_I_on_time()


# Inventory
def how_many():
    counter = 0
    for animal in myzoo.animals:
        counter += 1
    print("There are", counter, "animals for you to see today.")

how_many()

# Inventory by species


def by_species():
    myzoo.get_species_count()

by_species()

# Age by species


def age_by_species():
    max = 0
    name = 0
    for animal in myzoo.animals:
        if int(animal.age) > max:
            max = int(animal.age)
            name = animal.name
    print("Our oldest resident is", name, "at the merry old age of", max)

age_by_species()

### Age
def total_age():
    total_age = 0
    for animal in myzoo.animals:
        total_age += int(animal.age)
    print("The cumulative total age of our residents is:", total_age)

total_age()