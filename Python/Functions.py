# Nick May  - Harvard Course - May 2021

def square(x):
    return x * x

# user enters a number
y = int(input("Number: "))
print(square(y))

# or print a range of square numbers

for i in range(11):
    print(f"The square of {i} is {square(i)}")
