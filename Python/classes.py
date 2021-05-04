# Nick May  - Harvard Course - May 2021

#  class is a template for a type of object

# for this example think of a x/y point on an axis
# __init__ is a function that automaticallt runs when you try to do something, in this case create a new point


class Point():
    def __init__(self, x, y): # self references the object being worked upon ie: itself
        self.x = x
        self.y = y

p = Point(2, 8)

# to view the date inside p

print(p.x)
print(p.y)