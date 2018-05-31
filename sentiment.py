import pandas as pd
data = pd.read_excel(r'C:\Users\Ashika\Desktop\Project Delivery\AllComments.xlsm')
data1 = data['Comments']
all_pos = {}
all_neg = {}
happy_md = {}

allpositive = pd.read_excel(r'C:\Users\Ashika\Desktop\Project Delivery\Spero.xlsm',sheet_name='ALLPositive')
allnegative = pd.read_excel(r'C:\Users\Ashika\Desktop\Project Delivery\Spero.xlsm',sheet_name='ALLNegative')
happy = pd.read_excel(r'C:\Users\Ashika\Desktop\Project Delivery\Spero.xlsm',sheet_name='HAPPY')

for i,row in allpositive.iterrows():
    word = row['words']
    score = row['score']
    all_pos[word] = score

for i,row in allnegative.iterrows():
    word = row['words']
    score = -row['score']
    all_neg[word] = score


for i,row in happy.iterrows():
    word = row['WORD']
    score = row['SCORE']
    happy_md[word] = score

happy_md.update(all_neg)
happy_md.update(all_pos)
happy_md.items()

com1 = []
comm = list(data1)
for i in data1:
    i = i.split(' ')
    com1.append(i)


happy1 = list(happy['WORD'])
allpos1 = list(allpositive['words'])
allneg1 = list(allnegative['words'])


z = 0
splitnew = {}
newlist=[]
#for i in range(10000):
for i in com1[z]:
    for  j in happy1:
    #j = i.split('')
        if i==j:
            splitnew['new'] = com1[z]
            z = z+1
    break
    for  j in allpos1:
    #j = i.split('')
        if i==j:
            splitnew['new1'] = com1[z]
            z = z+1
    break
    for  j in allneg1:
    #j = i.split('')
        if i==j:
            splitnew['new2'] = com1[z]
    z = z+1
    print(i)

cpy = allpos1 + allneg1 + happy1

score = 0
avg = []
count = 0
for i in d:
    count = count +1
    for j in happy_md:
        if i !='to mark the end of a comment':
            if i==j:
                score = score + happy_md[i]
                #print(score)
    if i =="to mark the end of a comment":
        avg.append(score/count)
        print(avg)
        print(score)
        print(count)
        score = 0
        count = 0

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

dfcom1 = pd.DataFrame(avg,columns=['Scores'])
res = [data,dfcom1]
res1 = pd.concat(res,axis = 1)

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf

init_notebook_mode(connected=True)
cf.go_offline()
res1.iplot(kind='scatter',x='Comments',y='Scores',mode='markers',size=10)

