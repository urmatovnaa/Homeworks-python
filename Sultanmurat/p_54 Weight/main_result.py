from main import Weight

thing1 = Weight(1, 55, 120)
thing2 = Weight(1, 60, 55)

print(thing1 + thing2)
print(thing1 - thing2)

print(thing1 > thing2)
print(thing1 < thing2)
print(thing1 == thing2)
print(thing1 != thing2)
print(thing1 >= thing2)
print(thing1 <= thing2)

print(thing1.__str__())