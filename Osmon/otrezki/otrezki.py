a = [2, 168]
b = [
    [10, 15],
    [50, 78],
    [20, 32],
    [17, 29],
]
a = range(a[0], a[-1] + 1)
z = set(a)
counter = 0

while counter < 4:
    v = range(b[counter][0], b[counter][1] + 1)
    x = set(v)
    z.difference_update(x)
    counter += 1

print(len(z))
