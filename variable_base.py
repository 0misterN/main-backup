import random
from collections import defaultdict
from datetime import datetime


def gap(a1, a2):
    a = a1 - a2
    if a > 0:
        return a
    else:
        return a * -1
    
def create_num_as_list():
    l = []
    for i in range(0, 4):
        l.append(random.randint(0, 256))
    return l
    
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

def lsfra_round(m=list):
    c = 0
    
    while not m[0] == m[1] == m[2] == m[3]:
        m = lsfra_round_math(m)
        c += 1
    return c

def main(fcounter):
    d1 = defaultdict(int)
    d2 = {}
    n = 0
    while n < 10000000:
        tmp = create_num_as_list()
        c = lsfra_round(tmp)
        d2[list_to_int(tmp)] = c
        d1[c] += 1
        n += 1
    with open(f'c:\\Users\\bruec\\Documents\\codingPython\\lsfr_advanced\\tmp\\list_occurences_{fcounter}.txt', '+w') as f1:
        for item in sorted(d1.keys()):
            f1.write(f'{item}: {d1[item]}\n')
    with open(f'c:\\Users\\bruec\\Documents\\codingPython\\lsfr_advanced\\tmp\\list_appearences_{fcounter}.txt', '+w') as f2:
        for item in d2.keys():
            f2.write(f'{item}: {d2[item]}\n')
    with open('report.txt', 'a') as fa:
        fa.write(f'successfull at {datetime.now()}')
    
    return 0

if __name__ == '__main__':
    c = 0
    while True:
        main(c)  
        c += 1  
