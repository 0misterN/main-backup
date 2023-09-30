import matplotlib.pyplot as plt




def get_basic_probabilities(data):
    d = {}
    ls = data.split('\n')
    for item in ls:
        t = item.split(': ')
        if len(t) != 2:
            continue
        d[int(t[0])] = int(t[1])
    #print(d)
    return d

def get_averages(data=dict):
    num = 0
    for item in data.keys():
        num += data[item] 
    return num/len(data)

def plot_diagramm(dic=dict):
    x = [item for item in dic]
    y = [dic[item] for item in dic]
    print(x)
    a, ax1 = plt.subplots()
    ax1.bar(x, y, edgecolor = 'white')


    plt.show()

with open('d13.txt', 'r') as f:
    data = f.read()
    d = get_basic_probabilities(data)
    print(get_averages(d))
    plot_diagramm(d)
    