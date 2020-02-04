import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%\n{v:d}'.format(p=pct,v=val)
    return my_autopct

def repartition():
    labels = ['dockerfile', 'docker-compose', 'both', 'none']
    data = [15, 30, 40, 100]
    explode = (0, 0, 0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=labels, explode=explode, autopct=make_autopct(data), shadow=True, startangle=90)
    plt.title('Repartition of docker related files in the repositories')
    plt.show()

def keyword(data,totalRepos):
    #data is an array of arrays
    file = []
    compose = []
    both = []
    legends = []
    legendsLoc = []
    weights = [[],[],[]]
    weight = 1/totalRepos
    for i in range(len(data)):
        legendsLoc.append(i+1)
    for i in range(len(data)):
        legends.append(data[i][0])
        for j in range(data[i][1]):
            file.append(i+1)
            weights[0].append(weight)
        for j in range(data[i][2]):
            compose.append(i+1)
            weights[1].append(weight)
        for j in range(data[i][3]):
            both.append(i+1)
            weights[2].append(weight)
    bins = [x + 0.5 for x in range(0, len(data)+1)]
    plt.hist([file, compose, both], weights=weights,bins=bins, color=['royalblue', 'darkblue','blueviolet'], label=['dockerfile', 'docker-compose','both'],
                histtype='bar')  # bar est le defaut
    plt.ylabel('files containing the word')
    plt.title('Keyword by type of file')
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.xticks(legendsLoc,legends)
    plt.legend()
    plt.show()


#repartition()


x = [ ["mongo",1,3,2],["truc",2,0,1],["Florian",3,2,0],["test",1,1,3] ]

keyword(x,6)