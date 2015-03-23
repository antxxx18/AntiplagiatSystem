__author__ = 'Andriy'

def module(vect):
    s = 0
    for el in vect:
        s += vect[el] ** 2
    return s ** 0.5

def multi_cos(vect1, vect2):
    s = 0
    for el in set(vect1.keys()) & set(vect2.keys()):
        s += vect1[el]*vect2[el]
    if not module(vect1) or not module(vect2):
        return 0
    elif s / (module(vect1) * module(vect2)) > 1:
        return 1
    else:
        return s / (module(vect1) * module(vect2))