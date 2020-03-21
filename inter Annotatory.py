# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:42:12 2020

@author: jaswa
"""

import pandas as pd
import numpy as np

dat = pd.read_csv('Anno1.csv')


hasht = dat.values[:,1]
anno1 = dat.values[:,[0,1]]
anno2 = dat.values[:,[6,1]]


st = []

for i in hasht:
    
    j,k = i.split('_')
    j = j[4:]
    k = k.split('.')[0]
    st.append(k+j)


a1 = []
a2 = []
for i in range(len(st)):
    a1.append([st[i],anno1[i,0]])
    a2.append([st[i],anno2[i,0]])
    
dat2 = pd.read_csv('Annotation2.csv')


st1 = dat2.values[:,0]

anno3 = dat2.values[:,[0,2]]
a3 = []

for i in anno3:
    a3.append([i[0],i[1]])        
        

for i in range(len(a1)):
    if a1[i][1] == 'MULTIEVENT':
        a1[i][1] = 'EVENT'


for i in range(len(a2)):
    if a2[i][1] == 'MULTIEVENT':
        a2[i][1] = 'EVENT'


for i in range(len(a3)):
    if a3[i][1] == 'MULTIEVENT':
        a3[i][1] = 'EVENT'


anno=[]
for i in a1:
    anno.append(i)

for i in a2:
    anno.append(i)

for i in a3:
    if i[0] in st: 
        anno.append(i)
        

aa1 = {}
aa2 = {}
aa3 = {}

for i in a1:
    if i[0] not in aa1:
        aa1[i[0]] = []
        aa1[i[0]].append(i[1])
        

for i in a2:
    aa1[i[0]].append(i[1])
    

for i in a3:
    if i[0] in st:
        aa1[i[0]].append(i[1])
        
        

rt = dat2.values[:,5]

 

for i,j in aa1.items():
    if len(j) <3:
        print(i)


syn1 = pd.read_csv('Sync3_#kaala.csv') #298,130
syn3 = pd.read_csv('Sync1_#favpinoynewbieinigo.csv')#346,136
syn4 = pd.read_csv('Sync7_#travel.csv')#400,275
syn5 = pd.read_csv('Sync11_#travel.csv')#203,149
syn6 = pd.read_csv('Sync9_#travel.csv')#180,143
syn7 = pd.read_csv('Sync5_#travel.csv')#477
syn8 = pd.read_csv('Sync3_#travel.csv')#402
syn9 = pd.read_csv('Sync1_#thtraffic.csv')#123
syn10 = pd.read_csv('Sync2_#bangkok.csv')#167



        


syn = []
for i,j in aa1.items():
    if len(j)>2:
        syn.append(j)
        
import csv
with open('inter.csv', 'w', newline='') as myfile:
     wr2 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in syn:
         wr2.writerow(i)

x = pd.read_csv('Anno2.csv')
r = dat2.values[:,[0,1]]
                   
rt = {}
for i in r:
    rt[i[0]] = i[1]
final = {}
for i,j in aa1.items():
    if len(j)>2:
        k=0
        for p in j:
            if p == 'EVENT':
                k+=1
        if k>=2:
            final[i] = 'EVENT'
        else:
            final[i] = 'RANDOM'
            
            
            
f = dat2.values[:,[0,4]]
final = {}
for i in f:
    final[i[0]] = i[1]


r= dat2.values[:,]
rt = {}

event = []
non_event = []

for i,j in final.items():
    if j == 'EVENT':
        event.append([i,j])            
    else:
        non_event.append([i,j])

z = dat2.values[:,[0,5]]
rt = {}
for i in z:
    rt[i[0]] = i[1]
    
    
import random

r1 = random.sample(range(len(event)),int(len(event)/2))

r2 = random.sample(range(len(non_event)),int(len(non_event)/2))
  
    
l1 = []
l2 = []

for i in r1:
    l1.append(rt[event[i][0]])
    
for i in r2:
    l2.append(rt[non_event[i][0]])
    

m1 = np.mean(l1)
std1 = np.std(l1)

hyp1 = [m1-1.6*std1,m1+1.6*std1]
print(m1,std1)
pred1 = []
ac1 = []
for i in range(len(event)):
    if i not in r1:
        ac1.append('EVENT')
        if rt[event[i][0]]>hyp1[0] and rt[event[i][0]]<hyp1[1]:
            pred1.append('EVENT')
        else:
            pred1.append('RANDOM')   
            
for i in range(len(non_event)):
    if i not in r2:
        ac1.append('RANDOM')
        if rt[non_event[i][0]]>hyp1[0] and rt[non_event[i][0]]<hyp1[1]:
            pred1.append('EVENT')
        else:
            pred1.append('RANDOM') 

from sklearn.metrics import confusion_matrix

con1 = confusion_matrix(ac1,pred1)

p1 = con1[0,0]/(con1[0,0]+con1[1,0])
re1 = con1[0,0]/(con1[0,0]+con1[0,1])
print(p1,re1)
print(2*p1*re1/(p1+re1))


m2 = np.mean(l2)
std2 = np.std(l2)
hyp2 = [m2-1.5*std2,m2+1.5*std2]
print(m2,std2)

pred2 = []
ac2 = []
for i in range(len(event)):
    if i not in r1:
        ac2.append('EVENT')
        if rt[event[i][0]]>hyp2[0] and rt[event[i][0]]<hyp2[1]:
            pred2.append('RANDOM')
        else:
            pred2.append('EVENT')   
            
for i in range(len(non_event)):
    if i not in r2:
        ac2.append('RANDOM')
        if rt[non_event[i][0]]>hyp2[0] and rt[non_event[i][0]]<hyp2[1]:
            pred2.append('RANDOM')
        else:
            pred2.append('EVENT') 

from sklearn.metrics import confusion_matrix

con2 = confusion_matrix(ac2,pred2)
p2 = con2[0,0]/(con2[0,0]+con2[1,0])
re2 = con2[0,0]/(con2[0,0]+con2[0,1])
print(p2,re2)
print(2*p2*re2/(p2+re2))

event_rt = []
    
nirm = []
for i,j in aa1.items():
    if len(j)>2:
        nirm.append([i,j[0],j[1],j[2],final[i],rt[i]])
    
r = dat2.values[:,[0,1,3,4,5]]

rr = {}

k=0
for i in r[0]:
    rr[r[0]] = dat2.values[k,[1,3,4,5]]
    k+=1

with open('Annotations.csv', 'w', newline='') as myfile:
     wr2 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in nirm:
         wr2.writerow(i)
    
    
for i in range(len(event)):
    if i not in r1:
        ac2.append('EVENT')
        if rt[event[i][0]]>hyp1[1]:
            print(1)
k=0
for i in range(len(non_event)):
    if i not in r2:
        if rt[non_event[i][0]]>hyp2[1] :
            k+=1
            print(k)     
    


import seaborn as sns

sns.distplot(dat2['Rt/T'],bins= 20,kde=False)

event_rt = []
for i in event:
    event_rt.append(rt[i[0]])


non_event_rt = []
for i in non_event:
    non_event_rt.append(rt[i[0]])

sns.distplot(non_event_rt,bins= 20,kde=False,color = 'red')

sns.distplot(event_rt,bins= 20,kde=False,color = 'blue')


dat2 = pd.read_csv('Anno2.csv')
dat2 = dat2.values[:,[2,5]]


for i in range(len(dat2)):
    if dat2[i,0] == 'MULTIEVENT':
        dat2[i,0] = 'EVENT'
dat2 = []
for i,j in final.items():
    dat2.append([j,rt[i]])

k=0
for i in dat2:
    if i[1]>=0 and i[1]<=0.05:
        dat2[k][1] = '0-0.05'
    elif i[1]>0.05 and i[1]<=0.1:
        dat2[k][1] = '0.05-0.1'
    elif i[1]>0.1 and i[1]<=0.15:
        dat2[k][1] = '0.1-0.15'
    elif i[1]>0.15 and i[1]<=0.2:
        dat2[k][1] = '0.15-0.2'
    elif i[1]>0.2 and i[1]<=0.25:
        dat2[k][1] = '0.2-0.25'
    elif i[1]>0.25 and i[1]<=0.3:
        dat2[k][1] = '0.25-0.3'
    elif i[1]>0.3 and i[1]<=0.35:
        dat2[k][1] = '0.3-0.35'
    elif i[1]>0.35 and i[1]<=0.4:
        dat2[k][1] = '0.35-0.4'
    elif i[1]>0.4 and i[1]<=0.45:
        dat2[k][1] = '0.4-0.45'
    elif i[1]>0.45 and i[1]<=0.5:
        dat2[k][1] = '0.45-0.5'
    elif i[1]>0.5 and i[1]<=0.55:
        dat2[k][1] = '0.5-0.55'
    elif i[1]>0.55 and i[1]<=0.6:
        dat2[k][1] = '0.55-0.6'
    elif i[1]>0.6 and i[1]<=0.65:
        dat2[k][1] = '0.6-0.65'
    elif i[1]>0.65 and i[1]<=0.7:
        dat2[k][1] = '0.65-0.7'
    elif i[1]>0.7 and i[1]<=0.75:
        dat2[k][1] = '0.7-0.75'
    elif i[1]>0.75 and i[1]<=0.8:
        dat2[k][1] = '0.75-0.8'
    elif i[1]>0.8 and i[1]<=0.85:
        dat2[k][1] = '0.8-0.85'
    elif i[1]>0.85 and i[1]<=0.9:
        dat2[k][1] = '0.85-0.9'
    elif i[1]>0.9 and i[1]<=0.95:
        dat2[k][1] = '0.9-0.95'
    elif i[1]>0.95 and i[1]<=1:
        dat2[k][1] = '0.95-1'
    k+=1
    
o = {}
for i in dat2:
    o[i[1]] = 0

order = np.sort(list(o.keys()))
dat2[np.argsort(dat2[:,1])]

for i in event:
    if rt[i[0]] <=0.05:
        print(i[0])

d = pd.DataFrame(dat2,columns=['Label','Retweet Ratio'])

import matplotlib.pyplot as plt
plt.figure(figsize=(16,4)) # this creates a figure 8 inch wide, 4 inch high
sns.countplot(x='Retweet Ratio',hue='Label',data=d,order = order)
plt.savefig('plot.jpg')
plt.show()

dd = []

for i,j in aa1.items():
    if len(j)>2:
        dd.append([i,j[0],j[1],j[2],final[i],rt[i]])


with open('Final.csv', 'w', newline='') as myfile:
     wr2 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in dd:
         wr2.writerow(i)


