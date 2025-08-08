# Class method example

class Person:
    species = "Homo Sepnians"
    
    @classmethod
    def get_species(cls):
        print(cls)
        return cls.species
    
    
    def get_species2(self):
        return self.species
    

print(Person.get_species())


# print(Person.get_species2()) # will not run without an instance