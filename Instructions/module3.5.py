from math import sin
from random import randint


while int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : ")) != 42:
    print("Mauvaise réponse.")
print("Bravo !")

sum = 0
i = 0
num = int(input())
while num != -1:
    sum = sum + num
    i = i + 1
    num = int(input())
print(sum/i)


n = int(input())
for i in range(n):
    print('X' * n)


n = int(input())
e = -1
print('X' * n)
for i in range(n-1):
    n=n-1
    e=e+1
    print(' ' * e, 'X' * n)

n = int(input())
sum = 0
if n > 0:
    for i in range(n):
        n = int(input())
        sum = sum + n
    print(sum)
elif n == 0:
    print(0)
else:
    n = input()
    while n != 'F':
        sum = sum + int(n)
        n = input()
    print(sum)



NB_ESSAIS_MAX = 6
secret = randint(0, 100)
n = int(input())
for i in range(NB_ESSAIS_MAX):
    i = i + 1
    if n < secret and i < NB_ESSAIS_MAX:
        print('Trop petit')
        n = int(input())
    elif n > secret and i < NB_ESSAIS_MAX:
        print('Trop grand')
        n = int(input())
    else:
        if n == secret:
            print('Gagné en ', i, ' essais !')
            break
        else:
            print('Perdu ! Le secret était ', secret)


n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i * j, end=' ')
    print()
print()



x = float(input())
print(sin(x))
