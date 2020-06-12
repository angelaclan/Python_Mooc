import random
from math import sqrt
from random import randint, seed


def alea_dice(s):
    random.seed(s)
    result = []
    for i in range(3):
       result.append(random.randint(1,6))
    if 1 in result:
        if 2 in result:
            if 4 in result:
                return True
    return False

def rendre_monnaie(price, e1, e2, e3, e4, e5):
    paid_bill = e1*20 + e2*10 + e3*5 + e4*2 + e5*1
    if paid_bill < price:
        return (None, None, None, None, None)
    elif paid_bill == price:
        return (0, 0, 0, 0, 0)
    elif paid_bill > price:
        amount = paid_bill - price
        list = [20, 10, 5, 2, 1]
        new_list = []
        for each in list:
            if amount > 0:
                result = amount // each
                rest = amount - result * each
                amount = rest
                new_list.append(result)
            else:
                new_list.append(0)
        return new_list

def somme(a=0, b=1):
    return a + b

def rac_eq_2nd_deg(a, b, c):
    if 4*a*c > b**2:
        return ()
    else:
        x = ((-1*b) + sqrt((b**2)-(4*a*c))) / (2*a)
        y = ((-1*b) - sqrt((b**2)-(4*a*c))) / (2*a)
        if x == y:
            return x ,
        elif x < y:
            return x , y
        else:
            return y, x


def factorial(n):
    if (n <= 1):
        return 1
    return n * factorial(n - 1)


def catalan(n):
    return int(factorial(2 * n) / (factorial(n + 1) * factorial(n)))

def bat(joueur1, joueur2):
    if joueur1 == 0 and joueur2 == 2 :
        return True
    elif joueur1 == 1 and joueur2 == 0 :
        return True
    elif joueur1 == 2 and joueur2 == 1 :
        return True
    else:
        return False



dict = {
    0 : "Pierre",
    1 : "Feuille",
    2 : "Ciseaux"
}
point = {
    'bat' : 1,
    'battu' : -1,
    'annule' : 0
}
def bat(joueur1, joueur2):
    if joueur1 == joueur2:
        return 0
    if joueur1 == 0 and joueur2 == 2:
        return 1
    elif joueur1 == 0 and joueur2 == 1:
        return -1
    if joueur1 == 1 and joueur2 == 0:
        return 1
    elif joueur1 == 1 and joueur2 == 2:
        return -1
    if joueur1 == 2 and joueur2 == 0:
        return 1
    elif joueur1 == 2 and joueur2 == 1:
        return -1
def doOneTurn(coup1, coup2):
    result = bat(coup1, coup2)
    if result == 1:
        print("{0} bat {1} : {2}".format(dict[coup1], dict[coup2],result))
    elif result == -1:
        print("{0} est battu par {1} : {2}".format(dict[coup1], dict[coup2], result))
    else:
        print("{0} annule {1} : {2}".format(dict[coup1], dict[coup2],result))
    return result
s = int(input())
seed(s)
sum = 0
for i in range(5):
    coup1 = randint(0, 2)
    coup2 = int(input())
    result = doOneTurn(coup1, coup2)
    sum += result
if sum > 0:
    print('Gagne')
if sum == 0:
    print('Nul')
if sum < 0:
    print('Perdu')

