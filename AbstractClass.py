from abc import ABC, abstractmethod


# we cannot create object for abstract class
# classes inheriting abstract class must override all the abstract method
class Vehicle(ABC):

    # since this is decorated as abstractmethod all the class
    # inherits Vehicle class has to implement start method
    # implement stop method is not necessary.
    @abstractmethod  # decorator
    def start(self):
        pass

    def stop(self):
        pass


# it inherits Vehicle class , so it has to implement all the methods
# in the abstract class. if not implemented Bike class also
# treated as an abstract class.
class Bike(Vehicle):  # Concrete class
    color = None
    def start(self):
        print("you are driving a bike")


class Car(Vehicle):
    color = None
    def start(self):
        print("You are riding a Car...")
