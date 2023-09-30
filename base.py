import random
from collections import defaultdict

def gap(a1, a2):
    if a1 - a2 > 0:
        return a1 - a2
    else:
        return a2 - a1
    
def list_to_int(i=list):
    n = 0
    for c in range(0, len(i)):
        n += i[c] * 10 ** c
    return n

def int_to_list(t=int):
    l = []
    t = str(t)
    for i in range(0, 6-len(t)):
        l.append(0)
    for i in range(0, len(t)):
        l.append(int(t[i]))
    return l
    
def lsfra_round_math(l):
    l_new = [gap(l[-1], l[-2])]
    for i in range(0, len(l) - 1):
        l_new.append(l[i])
    return l_new

def lsfra_round(num):
    c = 0
    m = int_to_list(num)
    mg = m
    while not m[0] == m[1] == m[2] == m[3] == m[4] ==m[5]:
        m = lsfra_round_math(m)
        c += 1
    return mg, c

def main(fcounter):
    d1 = defaultdict(int)
    d2 = {}
    n = 0
    while n < 1000000:
        m, c = lsfra_round(n)
        d2[n] = c
        d1[c] += 1
        n += 1
    with open('d14.txt', 'w') as f1:
        for item in sorted(d1.keys()):
            f1.write(f'{item}: {d1[item]}\n')
    with open('d24.txt', 'w') as f2:
        for item in d2.keys():
            f2.write(f'{item}: {d2[item]}\n')
    print('successfull')


if __name__ == '__main__':
    main()
