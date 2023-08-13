def fizzbuzz(num1, num2, num3):
    result = ""
    for i in range(1, num3 + 1):
        if not i % num1 and not i % num2:
            result += "FB"
        elif not i % num1:
            result += "F"
        elif not i % num2:
            result += "B"
        else:
            result += str(i) + " "
    return result


# Відкриваємо файл для читання
with open("testfile.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.split()))
        if len(nums) == 3:
            result = fizzbuzz(nums[0], nums[1], nums[2])
            print(result)
