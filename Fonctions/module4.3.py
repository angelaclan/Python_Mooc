def deux_egaux(a, b, c):
    if a == b or b == c or a == c:
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())
print(deux_egaux(a, b, c))



def soleil_leve(a, b, c):
    if a == 0 and b == 0:
        return True
    elif a > b:
        if (a <= c and c <= 23) or (0 < c and c < b):
            return True
        else:
            return False
    elif a < b:
        if a <= c and c < b:
            return True
        else:
            return False
    else:
        return False


def premier(n):
    if n == 2:
        return True
    elif n > 2:
        list = []
        for i in range(2, n):
            if n % i == 0:
                list.append(i)
        if len(list) < 1:
            return True
    return False

x = int(input())
for i in range(x):
    if premier(i) == True:
        print(i)



def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibo(n - 1) + fibo(n - 2)

n = int(input())
for i in range(n):
    print(fibo(i))