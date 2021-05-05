# Nick May  - Harvard Course - May 2021
import sys

#importing sys so we can exit the program on an error

# lets get some inputs

x = int(input("X: "))
y = int(input("Y: "))

# try this first
###### result = x / y

###### print(f"{x} divided by {y} = {result}")


# however, if you enter x as 5 and y as 0 you will get a zero dividion error, it wont work.

# you could add a try except like this

try:
    result = x / y
except ZeroDivisionError:
    print("Error, cannot divide by 0")
    sys.exit(1)

print(f"{x} divided by {y} = {result}")

# you could also use a try on the input, to make sure the user enters an integer, not a world

try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError:
    print("A number, not a word you idiot!")
    sys.exit(1)
