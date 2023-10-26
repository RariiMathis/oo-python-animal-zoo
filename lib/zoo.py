from lib.animal import Animal

class Zoo:
    all = []

    def __init__(self, name ,location) :
        self.name = name
        self.location = location
        Zoo.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            raise ValueError("Must be a String")

    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, new_location):
        if type(new_location) == str:
            self._location = new_location
        else:
            raise ValueError("Must be a String")  

    def animals(self):
        results = []
        for animal in Animal.all:
            if animal.zoo == self:
                results.append(animal)
        return results
    def animal_species(self):
        results = []
        for animal in self.animals():
            results.append(animal.species)
        return list(set(results))
    def find_by_species(self, species):
        results =[]
        for animal in self.animal():
            if animal.species == species:
                results.append(animal)
        return set(results)
    def animal_nicknames(self):
        nicknames = []
        for animal in self.animals():
            nicknames.append(animal.nickname)
        return nicknames
    @classmethod
    def find_by_location(self, location):
        zoos = []
        for zoo in Zoo.all:
            if zoo.location == location:
                zoos.append(zoo)
        return zoos