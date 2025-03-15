#Create a SolarObject class with attributes for farthest distance from the sun (au), spin, and orbital time (days)
class SolarObject:
    def __init__(self, name, distance, orbit):
        self.name = name
        self.distance = distance
        self.orbit = orbit

#Create a 'colonization' method that calculates the potential population based on distance from the sun
    def colonization(self):
        return round((6000000000 / self.distance),2)

#Create a 'spin' method which just does a 'pass'
    def spin(self):
        pass

#Create two instances of a 'Planet' class using Earth and Mars. Using polymorphism, the planets always spin 'slightly elliptically'
class Planet(SolarObject):
    def __init__(self, name, distance, orbit):
        super().__init__(name, distance, orbit)
    def spin(self):
        return 'slightly elliptical'
    def __str__(self):
        return f'{self.name} is {self.distance} au from the sun, spins {self.spin()} and has an orbit taking {self.orbit} days and can support a population of {self.colonization()} billion'

earth = Planet('Earth', 1.02, 365)
mars = Planet('Mars', 1.67, 687)

#Create a class for comets that inherits all variables and methods of SolarObject. The comets spin 'like crazy'
class Comet(SolarObject):
    def __init__(self, name, distance, orbit):
        super().__init__(name, distance, orbit)
    def spin(self):
        return 'like crazy'
    def __str__(self):
        return f'{self.name} is {self.distance} au from the sun, spins {self.spin()} and has an orbit taking {self.orbit} years and can support a population of {self.colonization()} billion'

#Create two instances of the Comet class (Halley and Hale-Bopp). Print the instances showing the orbital period in years
halley = Comet('Halley', 35, 76)
halebopp = Comet('Hale-Bopp', 354, 2400)

#Print all four objects, listing their attributes and colonization potential
for object in [earth, mars, halley, halebopp]:
    print(object)