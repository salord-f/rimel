import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%\n{v:d}'.format(p=pct,v=val)
    return my_autopct

def repartitionPie(dockerfile, dockercompose, both, none):
    """takes the number of repositories containing a dockerfile, docker-compose, both or none
     plot the corresponding pie chart"""
    labels = ['dockerfile', 'docker-compose', 'both', 'none']
    data = [dockerfile, dockercompose, both, none]
    explode = (0, 0, 0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=labels, explode=explode, autopct=make_autopct(data), shadow=True, startangle=90)
    plt.title('Repartition of docker related files in the repositories')
    plt.savefig('graphs/repartitionPie.png')
    plt.show()

def keyword(data,labels,totalRepos,filename):
    """takes an array of arrays[name,nbDockerfile,nbDockerCompose,nbBoth] and the total number of repositories
     plot the corresponding histogram chart"""
    file = []
    compose = []
    both = []
    legends = []
    legendsLoc = []
    weights = [[],[],[]]
    for i in range(len(data)):
        legendsLoc.append(i+1)
    for i in range(len(data)):
        legends.append(data[i][0])
        file.append(i + 1)
        weights[0].append(int(data[i][1])/totalRepos)
        compose.append(i+1)
        weights[1].append(int(data[i][2])/totalRepos)
        both.append(i+1)
        weights[2].append(int(data[i][3])/totalRepos)
    bins = [x + 0.5 for x in range(0, len(data)+1)]
    plt.hist([file, compose, both], weights=weights,bins=bins, label=labels,histtype='bar',)
    plt.ylabel('Repositories containing the keyword')
    plt.title('Keyword by type of file')
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.xticks(legendsLoc,legends)
    plt.ylim(0, 1)
    plt.legend()
    plt.savefig('graphs/'+filename+'.png')
    plt.show()

def keyword_values(data, labels, totalRepos, filename):
    """same as Keyword but shows the values"""
    file = []
    compose = []
    both = []
    legends = []
    legendsLoc = []
    maxi = 0
    weights = [[], [], []]
    for i in range(len(data)):
        legendsLoc.append(i + 1)
    for i in range(len(data)):
        legends.append(data[i][0])
        file.append(i + 1)
        weights[0].append(int(data[i][1]))
        maxi = max(maxi, int(data[i][1]))
        compose.append(i + 1)
        weights[1].append(int(data[i][2]))
        maxi = max(maxi, int(data[i][2]))
        both.append(i + 1)
        weights[2].append(int(data[i][3]))
        maxi = max(maxi, int(data[i][3]))
    bins = [x + 0.5 for x in range(0, len(data) + 1)]
    plt.hist([file, compose, both], weights=weights, bins=bins, label=labels, histtype='bar', )
    plt.ylabel('Repositories containing the keyword')
    plt.title('Keyword by type of file')
    plt.xticks(legendsLoc, legends)
    plt.ylim(0, maxi)
    plt.legend()
    plt.savefig('graphs/' + filename + '.png')
    plt.show()

#repartitionPie(12,20,31,52)

x = [ ["mongo",1,3,2],["truc",2,0,1],["Florian",3,2,0],["test",1,1,3] ]
#keyword(x,6)