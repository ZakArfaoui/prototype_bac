import numpy as np
import pickle as pk

def saisir_n():
    n = int(input("donner n : "))
    if   2 <= n <= 10:
        return n
    return saisir_n()

def saisir():
    n = int(input("donner l and c : "))
    if   5 <= n <= 10:
        return n
    return saisir()

def verif(ch):
    test = True
    i = -1
    while test and i < len(ch)-1:
        i += 1
        test = "a" <= ch[i] <= "z" and  2 <= len(ch) <= 10
    return test

def distinc(ch):
    test = True
    i = -1
    while test and i < len(ch)-1:
        i += 1
        test = ch.find(ch[i]) == i
    return test

def saisir_ch():
    test = False
    while not test:
        ch = input("donner une chaine : ")
        test = verif(ch) and distinc(ch)
    return ch

def fill_file(src, n):
    f1 = open(src, "w")
    for i in range(n):
        ch = saisir_ch()
        f1.write(ch + "\n")
    f1.close()

def fill_mat(src, m, n):
    f1 = open(src, "r")
    for i in range(n):
        ch = f1.readline()[:-1]
        while len(ch) < n:
            ch =  ch + "*"
        for j in range(n):
            m[i,j] = ch[j]      
    print(m)

def cryptch(ch):
    s = ""
    for i in range(len(ch)):
        s = s + chr(ord(ch[i]) + 2)
    return s
        

def crypt(m, src1, n):
    f2 = open(src1, "wb")
    ch = ""
    for i in range(n):
        for j in range(n):
            ch = ch = m[i,j]
            print(ch)
            cryp = cryptch(ch)
        e = {"chaine" : ch, "crpter": cryp }
        pk.dump(e, f2)
    f2.close()

def printing(src1):
    f2 = open(src1, "rb")
    try:
        e = pk.load(f2)
        while e != "":
            print(e)
            e = pk.load(f2)
    except:
        f2.close()


            

src  = "txt.txt"
src1 = "crypt.dat"
n = saisir_n()
# l = saisir()
# c = saisir()
m = np.array([[str]*n]*n)
fill_file(src, n)
fill_mat(src, m, n)
crypt(m, src1, n)
printing(src1)

