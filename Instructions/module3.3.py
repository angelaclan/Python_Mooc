from math import sqrt
from random import randint,randrange


a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print(a)
elif a == b or a == c:
    print(a)
elif b == c:
    print(c)


temp = int(input())
if temp > 0 and temp <= 10 :
    print('Il va faire frais')
elif temp <= 0 :
    print('Il va faire froid')


a = int(input())
b = int(input())
c = int(input())
if c == 1 :
    print(a + b)
elif c == 2 :
    print (a - b)
elif c == 3 :
    print (a * b)
elif c == 4 :
    print (a**2 + a * b)
elif c > 4 or c <= 0 :
    print('Erreur')


a = int(input())
if a%2 == 0 :
    print (True)
elif a%2 > 0  :
    print (False)

a = int(input())
b = int(input())
if b%a == 0 or a%b == 0 :
    print (False)
else:
    print (True)



a = float(input())
b = float(input())
if a < 0 or b < 0 :
    print ('Erreur')
else:
    print (sqrt(a*b))



n_pari = int(input())
n_issu = int(input())
ROUGE = {1,3,5,7,9,12}
NOIR = {2,4,6,8,10,11}

if n_pari == n_issu:
    print (10 * 12)
elif n_pari == 13 and n_issu%2 == 0:
    print (10 * 2)
elif n_pari == 14 and (n_issu%2 > 0 or n_issu == 1):
    print (10 * 2)
elif n_pari == 15 and n_issu in ROUGE:
    print (10 * 2)
elif n_pari == 16 and n_issu in NOIR:
    print (10 * 2)
else:
    print (0)


p = str(input())
a = float(input())
if p == 'T':
    print((sqrt(2)/12) * a**3)
elif p == 'C' :
    print(a**3)
elif p == 'O' :
    print((sqrt(2)/3) * a**3)
elif p == 'D' :
    print(((15+7*sqrt(5))/4) * a**3)
elif p == 'I' :
    print((5*(3+sqrt(5))/12) * a**3)
else :
    print("Polyèdre non connu")