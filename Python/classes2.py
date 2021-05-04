# Nick May  - Harvard Course - May 2021

# creating a class for an airline that wants to book the correct number of seats for the flight

# for OOP the Object is the flight and we add methods for dealing with issues on the flight, in this case seats available.

class Flight():
    def __init__ (self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats(): # if open seats == 0
            return False # False means no seats available
        self.passengers.append(name)
        return True # True means seats are available

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

# lets add passengers

people = ["John", "Paul", "Ringo", "George"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to the flight")
    else:
        print(f"Flight is full {person} not added")
