def transcription_arn(brin):
    brin = brin.replace('T', 'U')
    return brin

def plus_grand_bord(w):
    n = len(w)
    for i in range(1, n):
        if w[:n-i] == w[i:]:
            return w[:n-i]
    return ''

def premier(n):
    if int(n)==2:
        return True
    elif int(n)>2:
        list = []
        for i in range(2, n):
            if n % i == 0:
                list.append(i)
        if len(list) < 1:
            return True
    return False

def prime_numbers(nb):
    if int(nb) > 0:
        collection = []
        i = 1
        while len(collection) != nb:
            i = i + 1
            if premier(i) == True:
                collection.append(i)
        return collection
    elif nb == 0:
        return []
    else:
        return None
