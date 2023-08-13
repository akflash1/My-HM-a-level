#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
def solution(a):
    solution = [a[i:i+2] for i in range(0, len(a), 2)]
    if len(a) % 2 != 0:
        solution[-1] += '_'
    return solution

a = 'abcdefj'
print(solution(a))