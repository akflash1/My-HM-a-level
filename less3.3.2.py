a = int(input("Яку суму бажаєте отримати: "))
banknotes = [(1000, "One thousand"), (500, "Five hundred"), (200, "Two hundred"), (100, "One hundred")]

for banknotes, symbol in banknotes:
    result = a // banknotes
    a %= banknotes
    if result > 0:
        print(f"{result} = {symbol}")