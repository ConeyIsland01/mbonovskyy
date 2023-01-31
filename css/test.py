print("Hello world")
from functools import reduce
tor = lambda x: x + x**10
print(tor(5))
def yolo(c):
    return c*10000
def yolo3(c):
    if c > 2:
        pass
    else:
        return c

li = [4, 3, 2, 1,8,23,232,11,3]

print(list(map(yolo, li)))

print(list(filter(yolo3, li)))
bro = lambda x, z: x+z
print(bro(3,4))
print(reduce(lambda x, z: x+z, li))
r=0
for x in li:
    r += x
print(r)