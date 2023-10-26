class Animal:
    all = []

    def __init__(self, species , weight, nickname, zoo) :
        self.nickname = nickname
        self.weight = weight
        self.species = species
        self.zoo = zoo
        Animal.all.append(self)

    @property
    def nickname(self):
        return self._nickname
    @nickname.setter
    def nickname(self, new_nickname):
        if type (new_nickname) == str:
            self._nickname = new_nickname
        else:
            raise ValueError("This is not a String")    

    @property
    def species(self):
        return self._species
    @species.setter
    def species(self, new_species):
        if hasattr(self, "_species"):
            raise ValueError("Can not overwrite species")
        else:
            self._species = new_species
    @classmethod
    def find_by_species(cls, species):
        results = []
        for animal in Animal.all:
            if animal.species == species:
                results.append(animal)
        return results            
