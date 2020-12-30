def collatz(a):
    if a % 2 == 0:
        return int(a / 2)
    else:
        return 3 * a + 1


z = 9
r = []
while z > 1:
    z = collatz(z)
    r.append(z)
print(r)
