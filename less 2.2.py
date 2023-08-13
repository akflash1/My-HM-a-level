a = int(input("Введіть число: "))
i = 1
b = a % 10
c = (a // 10) % 10
x = a // 100

print("Розряди числа a:", x, c, b)

while i <= b:
    if b % i == 0:
        print("Множники числа b:", i)
    i += 1

i = 1

while i <= c:
    if c % i == 0:
        print("Множники числа c:", i)
    i += 1

i = 1

while i <= x:
    if x % i == 0:
        print("Множники числа x:", i)
    i += 1