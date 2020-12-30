def collatz(number):
    if number % 2 == 0:
        return number // 2
    return 3 * number + 1


zahl = 9
result = []
while zahl > 1:
    zahl = collatz(zahl)
    result.append(zahl)
print(result)
