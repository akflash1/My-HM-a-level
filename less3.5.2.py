def fizzbuzz(num1, num2, num3):
    return ' '.join(['FB' if not i % num1 and not i % num2 else 'F' if not i % num1 else 'B' if not i % num2 else str(i) for i in range(1, num3 + 1)])
