fizz = int(input("Введіть число: "))
buzz = int(input("Введіть число: "))
dizz = int(input("Введіть число: "))

for i in range(1, dizz + 1):

   if   i % fizz == 0 and i % buzz == 0:
       print("FВ")


   elif i % buzz == 0:
       print("B")


   elif  i % fizz == 0:
       print("F")

   else:
       print(i)

