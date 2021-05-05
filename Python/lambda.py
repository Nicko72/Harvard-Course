# Nick May  - Harvard Course - May 2021

# this is a dictionary nested inside a list

people = [
    {"name": "John", "house": "red"}, 
    {"name": "Paul", "house": "blue"}, 
    {"name": "Ringo", "house": "yellow"},
    {"name": "George", "house": "blue"}
    ]

# if you try and sort like this people.sort() you will get an error, so we need to tell python how to sort this dictionary

def f(person):
    return person["name"]

# now we have a function that will sort by name, we run this type of sort

people.sort(key=f)

print(people)

# now it is sorted by name - George will come first
# you could change the sort by changing return person["name"] to return person["house"] this will sort by house

# NOW python will let you do all of this on one line called a lambda this is how we could have done it:

people.sort(key=lambda person: person["name"]) # This is a fast way to do the same function

print(people)


