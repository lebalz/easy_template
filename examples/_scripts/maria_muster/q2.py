def collatz(num)
   if num % 2 == 0:
        return num / 2
    return (3 * num) + 1


res = []
zahl = 9
while zahl > 1
   zahl = collatz(zahl)
    res.append(zahl)
print(res)
