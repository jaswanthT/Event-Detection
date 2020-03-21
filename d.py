# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 23:15:41 2020

@author: jaswa
"""

import pandas as pd
import csv

data = pd.read_csv('Survey Results.csv')

d = data.values[:,:]

thres = 17

result1 = []
for i in d[0:211]:
    if i[1] >= thres:
        if i[2] >=(i[1]/2):
            result1.append([int(i[0]-1),'EVENT'])
        else:
            result1.append([int(i[0]-1),'MULTIEVENT'])
    else:
        result1.append([int(i[0]-1),'RANDOM'])
        
        
result2 = []
for i in d[211:]:
    if i[1] >= thres:
        if i[2] >=(i[1]/2):
            result2.append([int(i[0]-211-1),'EVENT'])
        else:
            result2.append([int(i[0]-211-1),'MULTIEVENT'])
    else:
        result2.append([int(i[0]-211-1),'RANDOM'])


with open('result1.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in result1:
         wr.writerow(i)
        
with open('result2.csv', 'w', newline='') as myfile:
     wr2 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in result2:
         wr2.writerow(i)
         
         
hasht = pd.read_csv('survey_ease_data.csv')

h = hasht.values[:,1]
tags= []
for i in range(len(h)):
    if i%2 == 0:
        tags.append(h[i])
        
with open('tags.csv', 'w', newline='') as myfile:
     wr2 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in tags:
         wr2.writerow([i])
         
dat = pd.read_csv('d.csv',header=None)
dic = {}
dat = dat.values[:,:]
for i in tags:
    dic[i] = []
    
for i in dat:
    dic[i[5]].append(i)
    
    
list1 = []
list2 = []

for i,j in dic.items():
    list1.append(list(j[0]))
    list2.append(list(j[1]))
    
with open('list1.csv', 'w', newline='') as myfile:
     wr2 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in list1:
         wr2.writerow(i)
         
with open('list2.csv', 'w', newline='') as myfile:
     wr2 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in list2:
         wr2.writerow(i)