# Programming Examn 1

Name: Maria Muster

Grade: 3

## Question 1

Points: 0.75 / 2

```py
print('hello maria')
```

## Question 2

Points: 3 / 3

```py
Answer                   | Solution
-----------------------------------------------------
def collatz(num)         | def collatz(number):
   if num % 2 == 0:      |     if number % 2 == 0:
        return num / 2   |         return number // 2
    return (3 * num) + 1 |     return 3 * number + 1
                         |
                         |
res = []                 | zahl = 9
zahl = 9                 | result = []
while zahl > 1           | while zahl > 1:
   zahl = collatz(zahl)  |     zahl = collatz(zahl)
    res.append(zahl)     |     result.append(zahl)
print(res)               | print(result)
```
