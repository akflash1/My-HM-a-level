def spam(number):
    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''
    return ''.join(['bulochka' for i in range(number)])


from functools import reduce
def my_sum(list_of_numbers):
    result = reduce(lambda x, y: x + y, list_of_numbers)
    return result



def shortener(string):
    words = string.split()
    res = []

    for word in words:
        if len(word) > 6:
            shortened_word = word[:6] + '*'
            res.append(shortened_word)
        else:
            res.append(word)

    return ' '.join(res)



def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count


