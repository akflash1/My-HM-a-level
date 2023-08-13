import sys
filename = sys.argv [0]
# далі відкриваємо файл для читання (опція 'r')

with open('file.txt','r') as f:

    prog = f.read()
    prog1 = prog[::-1]


print(prog1)