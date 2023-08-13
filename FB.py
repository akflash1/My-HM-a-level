def fizzbuzz(num1, num2, num3):
    result = ' '.join(map(lambda x: 'FB' if x % num1 == 0 and x % num2 == 0 else 'F' if x % num1 == 0 else 'B' if x % num2 == 0 else str(x), range(1, num3 + 1)))
    return result


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

print(fizzbuzz(num1, num2, num3))

