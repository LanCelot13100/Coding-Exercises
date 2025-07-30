#  Here is the basic representation of a class and the '__repr__' dunder method
#  class 'Person' has 'name', 'surname' and 'job' attributes and also the 'repr method' that shows us the technical info about the instance

class Person:
    def __init__(self,name,surname,job):
        self.name = name
        self.surname = surname
        self.job = job

    def __repr__(self):
        return f"Person {self.__dict__}"

p1 = Person("John","Smith","Taxi Driver")
print(p1)
