import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

def get_averages(data=dict):
    num = 0
    for item in data.keys():
        num += data[item] 
    return num/len(data)

def plot_diagramm(dic=dict):
    x = [item for item in dic]
    y = [dic[item] for item in dic]
    d = {'x': x, 'y': y}
    frame = pd.DataFrame(data=d)
    print(frame)
    sns.relplot(data=frame, x='x', y='y')
    plt.show()


with open('d23.txt', 'r') as f:
    data = f.read()
    d = get_basic_probabilities(data)
    #print(get_averages(d))
    plot_diagramm(d)
    