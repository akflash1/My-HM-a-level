#https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
def find_outlier(integers):
    even = [x for x in integers if x % 2 == 0]
    odd = [x for x in integers if not x % 2 == 0]
    if len(even) == 1:
        return even[0]
    else:
        return odd[0]
