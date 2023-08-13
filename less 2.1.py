x = int(input("Введіть число: "))
i = 1
while i <= x:
    if x % i == 0:
        print(i)
    i += 1