class Lion:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age


class Elephant:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age


class Tiger:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age


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

# myzoo = Zoo("9:00", "17:00")
# myzoo.add_animal(mylion)
# myzoo.add_animal(mylion2)
# myzoo.add_animal(myelephant)
# myzoo.get_species_count()
# myzoo.get_all_animals()
