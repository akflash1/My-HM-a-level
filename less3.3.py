a = int(input("Яку суму бажаєте отримати: "))
b = 1000
v = 500
j = 200
s = 100

res1 = a // b
res2 = (a - res1 * b) // v
res3 = (a - res1 * b - res2 * v) // j
res4 = (a - res1 * b - res2 * v - res3 * j) // s

if res1 > 0:
    print(f"{res1} * {b}")

if res2 > 0:
    print(f"{res2} * {v}")

if res3 > 0:
    print(f"{res3} * {j}")

if res4 > 0:
    print(f"{res4} * {s}")