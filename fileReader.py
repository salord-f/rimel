import sys
import graphs

file = open(sys.argv[1], "r")
content = file.readlines()
labels = content[0].split(';')[1:]
values = []
for i in range(1,len(content)):
    values.append(content[i].split(";"))

graphs.keyword(values,labels,100,"testValues")