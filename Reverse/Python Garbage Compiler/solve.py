import string
from random import *

def finalstage(w):
    h = 0
    w = list(w)
    w.reverse()
    w = "".join(g for g in w)
    flag = ''

    while h < len(w):
        try:
            flag += w[h+1] + w[h]
        except:
            flag += w[h]
        h += 2
    return flag

def stage2(b):
    t = ""
    seed(10)
    
    for q in range(len(b)):
        t += chr(ord(b[q])-randint(0,5))
    
    flag = finalstage(t)
    return flag

def stage1(a):
    a = list(a)
    b = list(string.ascii_lowercase)
    
    for o in range(len(a)):
        a[o] = chr(ord(a[o])^o)
    
    z = "".join(x for x in a)
    
    for y in range(len(z)):
        b[y%len(b)] = chr((ord(z[y])^ord(a[y]))+len(b))
    
    flag = stage2(z)
    return flag


def entry(f):
    seed(10)
    f = list(f)
    f.reverse()
    f = "".join(i for i in f)
    
    flag = stage1(f)
    return flag

def decrypt_finalstage(flag):
    h = 0
    flag = list(flag)
    decrypted = ''

    while h < len(flag):
        try:
            decrypted += flag[h+1] + flag[h]
        except:
            decrypted += flag[h]
        h += 2

    decrypted = list(decrypted)
    decrypted.reverse()
    decrypted = "".join(g for g in decrypted)
    
    return decrypted

def decrypt_stage2(b):
    seed(10)
    t = ""
    
    for q in range(len(b)):
        t += chr(ord(b[q])+randint(0,5))
    return t

def decrypt_stage1(z):
    a = list(z)
    b = list(string.ascii_lowercase)
    
    for y in range(len(z)):
        b[y%len(b)] = chr(((ord(z[y])^ord(a[y]))-len(b)) % 0x110000)    
    for o in range(len(a)):
        a[o] = chr(ord(a[o])^o)
    
    flag = "".join(x for x in a)
    return flag

def decrypt_entry(f):
    f = list(f)
    f.reverse()
    f = "".join(i for i in f)
    return f

if __name__ == '__main__':
    flag = open('output.txt', 'r').readlines()[0]
    decrypted_flag = (((decrypt_entry(decrypt_stage1(decrypt_stage2(decrypt_finalstage(flag)))))))
    input = entry(decrypted_flag)

    if input == flag:
        print("What... how?")
        print("I guess you broke my 'beautiful' code :(")
        print(decrypted_flag)
    else:
        print("haha, nope. Try again!")
