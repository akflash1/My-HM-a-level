from functools import reduce

def get_sum(a, b):
    result = reduce(lambda x, y: x + y, (a, b))
    return result

a = -1
b = 7

print(get_sum(a,b))

#https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python