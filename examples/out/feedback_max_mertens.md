# Programming Examn 1

Name: Max Mertens

Grade: 4

## Question 1

Points: 1.5 / 2

```py
print('hello max')
```

## Question 2

Points: 1 / 3

```py
Answer                    | Solution
------------------------------------------------------
def collatz(a):           | def collatz(number):
    if a % 2 == 0:        |     if number % 2 == 0:
        return int(a / 2) |         return number // 2
    else:                 |     return 3 * number + 1
        return 3 * a + 1  |
                          |
                          | zahl = 9
z = 9                     | result = []
r = []                    | while zahl > 1:
while z > 1:              |     zahl = collatz(zahl)
    z = collatz(z)        |     result.append(zahl)
    r.append(z)           | print(result)
print(r)                  |
```
