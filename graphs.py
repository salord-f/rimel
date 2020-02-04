import matplotlib.pyplot as plt
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

def motcle():
    plt.show()


repartition()
#motcle()