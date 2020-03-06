import sys
import graphs
import xlrd

if len(sys.argv) == 1:
    print("Please give the file path as the first argument")
    exit(0)

path = sys.argv[1]

if path.split('.')[1] == 'csv':
    file = open(sys.argv[1], "r")
    content = file.readlines()
    temp = content[0].split(';')
    repos = int(temp[0])
    labels = temp[1:]
    values = []
    for i in range(1, len(content)):
        values.append(content[i].split(";"))

else:
    sheet = xlrd.open_workbook(sys.argv[1]).sheet_by_index(0)
    repos = sheet.cell_value(0,0)
    labels = []
    for i in range(1, sheet.ncols):
        labels.append(sheet.cell_value(0, i))
    values = []
    for i in range(1, sheet.nrows):
        row = []
        for j in range(sheet.ncols):
            row.append(sheet.cell_value(i, j))
        values.append(row)

graphs.keyword(values, labels, repos, "KeywordHist")
graphs.keyword_values(values, labels, repos, "KeywordHistValues")
