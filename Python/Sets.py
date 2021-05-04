# Nick May  - Harvard Course - May 2021

# create an empty set
s = set()

# add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

print(s)

# no element evey appears twice, so if it add 3 again, it will not appear

s.add(3)
print(s)

# to remove an element
s.remove(2)
print(s)

#formatted string used to show the length

print(f"The set has {len(s)} elements")
