import matplotlib.pyplot as plt
from collections import defaultdict
plt.style.use('_mpl-gallery')


def get_basic_probabilities(data):
    dic = defaultdict(int)
    for i in range(0, len(data)):
        char = data[i]
        dic[char] += 1
    return dic
    
def sort_dic(dic=dict):
    ls = sorted(dic.keys())
    new_dic = {}
    for item in ls:
        new_dic[item] = dic[item]
    return new_dic

def print_dic(dic=dict):
    c = 0
    chars = sorted({chr(i) for i in range(128)} )
    for key in dic.keys():
        t = key
        if key <= 127:
            t = bytes(chars[t],encoding='ascii')
        print(f'{t}: {dic[key]}')
        c+= 1
        if c >= 100:
            break

def plot_diagramm(dic=dict):
    x = [item for item in dic]
    y = [dic[item] for item in dic]
    fig, ax1 = plt.subplots()
    ax1.bar(x,y, width = 1, edgecolor = 'white', linewidth=1)
    plt.show()
    print(x)
    print(y)

with open('ciphertext.txt', 'rb') as f:
    data = f.read()
    d = get_basic_probabilities(data)
    d = sort_dic(d)
    c = 0
    for n in [d[item] for item in d]:
        c+= n
    print(c)
    plot_diagramm(d)
   