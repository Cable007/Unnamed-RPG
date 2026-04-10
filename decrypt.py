from math import *
from ab import key
def decrypt(e, k):
    integer = isqrt(int(e, 16))
    s = str(integer)
    ns = []
    i = 0
    while i < len(s):
        if i + 2 <= len(s):
            t = int(s[i:i+2])
            if t in k.u or t in k.l:
                ns.append(t)
                i += 2
                continue
        if i + 3 <= len(s):
            tr = int(s[i:i+3])
            if tr in k.l:
                ns.append(tr)
                i += 3
                continue
    return "".join(chr(n) for n in ns)
print(decrypt("0x61dbdf2eb22738476d99", key))