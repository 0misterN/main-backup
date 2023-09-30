import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import threading
from collections import defaultdict
sns.set_theme(style="darkgrid")



def get_basic_probabilities(data):
    d = {}
    ls = data.split('\n')
    for item in ls:
        t = item.split(': ')
        if len(t) != 2:
            continue
        d[int(t[0])] = int(t[1])
    
    return d

def get_dic(file):
    with open(file, 'r') as f:
        data = f.read()
    return get_basic_probabilities(data)

def compare(l1, l2):
    for i in range(0, len(l1)):
        if not i in l2:
            l2.append(i)
    return l2

###
def combine_dict_keys(d1=dict, d2=dict):
    print('processing dicts')
    res_dict = defaultdict(int)
    res_keys = compare(list(d1.keys()), list(d2.keys()))
    for item in res_keys:
        try:
            res_dict[item] += d1[item]
        except KeyError:
            pass
        try:
            res_dict[item] += d2[item]
        except KeyError:
            pass
    return res_dict
###

def main():
    dir = os.listdir('c:\\Users\\bruec\\Documents\\codingPython\\lsfr_advanced\\tmp')
    for item in dir:
        if item.find('occurrences') == -1:
            dir.remove(item)
    n = len(dir)
    even = 1 - (n % 2) 
    dn = {}

    if even:
        for i in range(0, n, 2):
            d1 = get_dic(dir[i])
            d2 = get_dic(dir[i+1])
            dn[i] = combine_dict_keys(d1, d2)
            
        while len(dn) != 1:
            for c in range(0, len(dn), 2):
                tmp = combine_dict_keys(dn[c], dn[c])
                dn.
            ### work with classes!!!
            

if __name__ == '__main__':
    main()