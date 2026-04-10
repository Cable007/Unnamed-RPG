from math import *
from ab import key
def encrypt(w, k):
    output = ""
    for c in w:
        ca = ord(c)
        if ca in k.l:
            i = k.l.index(ca)
            output += str(k.l[i])
        elif ca in k.u:
            i = k.u.index(ca)
            output += str(k.u[i])
        else:
            output += c
    integer = int(output)**2
    return hex(integer)
print(encrypt("Cable", key))