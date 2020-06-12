from math import sqrt

def signature(identite):
    (nom, prenom) = identite
    return prenom + ' ' + nom

def est_adn(compo):
    if compo == '':
        return False
    for each in compo:
        if each !='A' and each !='C' and each !='G'and each !='T':
            return False
    return True


def duree(start, end):
    (hour, minute) = start, end
    if start[0] < end[0]:
        if end[1] < start[1]:
            tempH = end[0] - 1
            minute = 60 - start[1] + end[1]
            hour = tempH - start[0]
            return (hour, minute)
        else:
            hour = end[0] - start[0]
            minute = end[1] - start[1]
            return (hour, minute)
    elif start[0] >= end[0]:
        tempM = 60 - start[1]
        minute = tempM + end[1]
        tempH = 23 - start[0]
        hour = tempH + end[0]
        if minute >= 60:
            minute == 0
            hour + 1
        return (hour, minute)


def distance_points(point1, point2):
    (x, y) = point1, point2
    dp = sqrt(((x[0]-y[0])**2) + ((x[1]-y[1])**2))
    return dp