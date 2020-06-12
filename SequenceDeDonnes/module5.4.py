def anagrammes(v, w):
    x = list(w)
    if len(v) == len(x):
        for letter in v:
            if letter in x:
                x.remove(letter)
        if len(x) == 0:
            return True
    return False

def dupliques(para):
    for i in range(len(para)-1):
        for each in para:
            if para[i] in para[i+1:]:
                return True
    return False

def my_insert(lst, n):
    if n % 1 is 0:
        lst.append(n)
        new_list = lst
        new_list.sort()
        return new_list
    return None

def distance_mots(mot_1, mot_2):
    if len(mot_1) == len(mot_2):
        x = 0
        for i in range(len(mot_1)):
            if mot_1[i] != mot_2[i]:
                x = x +1
        return x


def distance_mots(mot_1, mot_2):
    if len(mot_1) == len(mot_2):
        x = 0
        for i in range(len(mot_1)):
            if mot_1[i] != mot_2[i]:
                x = x + 1
        return x


def correcteur(mot, liste_mots):
    for each in liste_mots:
        if len(each) == len(mot) and distance_mots(mot, each) < 2:
            return each
    return mot
