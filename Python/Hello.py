print("Hello, World!")

name = input("Name: ")

print(name, "is your name")

# f string is a formatted string and substitutes the variable for the value input

print(f"{name} is your name")

n = int(input("Number: "))

if n > 0:
    print(f"{n} is positive")
elif n < 0:
    print(f"{n} is negative")
else:
    print(f"{n} is zero")

beetles = ["John", "Paul", "Ringo"]

print(beetles[0])

print(beetles[0][0]) #2 dimensional array