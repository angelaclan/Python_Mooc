def my_pow(m, b):
    if type(m) == int and type(b) == float:
        return [b**i for i in range(m)]
    return None

def flatMap(ll):
    lst = []
    for l in ll:
        lst = lst + l
    return lst
def decompresse(lt):
    return flatMap ([[t[1]] * t[0] for t in lt])

def my_filter(lst, f):
    return ([i for i in lst if f(i) is True])