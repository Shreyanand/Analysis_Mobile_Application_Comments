#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 16:18:08 2018

@author: shrey
"""
import csv
import re

path = "/Users/shrey/Desktop/Limbic-master/outputapp/CNNtopwords_20_0.1.txt"
with open(path) as f:
    content = f.readlines()

content = [x.strip() for x in content]    
aspect = {}
c = 0
for i in  range(4,44,2):
    pos = content[i].split(',')
    neg = content[i+40].split(',')
    pos.append(content[i-1])
    neg.append( content[i+39])
    aspect[c] = (pos,neg)
    c += 1

aspectcomment = False 
asenti = {}  
username = "NILL"     
for i in content:
    if re.fullmatch('User-Sentiment-Aspect Clusters \(relative order\):',i):
        break
    if re.fullmatch('User-Sentiment-Aspect Clusters:',i):
        aspectcomment = True
    if (aspectcomment):
        #print(i)
        values = False
        res = re.search('Users/shrey/Desktop/Limbic-master/input/segment/CNNDataIndexed/(.*).txt', i)
        if (res):
            username = res.group(1)
            values = False            
        else:            
            values = True
        if (values):
            if username in asenti:
                asenti[username].append(i)
            else:
                asenti[username] = [i]

del asenti['NILL']
del asenti['comments']
                
for i in asenti:
    a = asenti[i]
    if '' in a:
        asenti[i].remove('')  
    a[1] = a[1].split(',')
    a[3] = a[3].split(',')
    
    for j in range(len(a[1])):
        a[1][j] = a[1][j].split(':')[1]   
       
    for j in range(len(a[3])):
        a[3][j] = a[3][j].split(':')[1]
    
    maxi = max(a[1])
    a[1] = [k for k, l in enumerate(a[1]) if l == maxi]
    
    maxi = max(a[3])
    a[3] = [k for k, l in enumerate(a[3]) if l == maxi]
        
    del a[0]
    del a[1]
        
pos_aspects = {}
neg_aspects = {}
for i,j in asenti.items():
    
    for k in j[0]:
        if k in pos_aspects:
            pos_aspects[k].append(i)
        else:
            pos_aspects[k] = [i]
            
    for k in j[1]:
        if k in neg_aspects:
            neg_aspects[k].append(i)
        else:
            neg_aspects[k] = [i]

pos_aspects_comments = {}
neg_aspects_comments = {}

for i in pos_aspects:
    for j in pos_aspects[i]:
        file_path = "/Users/shrey/Desktop/Limbic-master/input/segment/CNNSingularEmbedded/" + j + ".txt"
        with open(file_path, 'r', encoding='utf8') as f:
            content = f.read()
            content = content.replace('\n',' ')
        if i in pos_aspects_comments:
            pos_aspects_comments[i].append(content)
        else:
            pos_aspects_comments[i] = [content]
            
for i in neg_aspects:
    for j in neg_aspects[i]:
        file_path = "/Users/shrey/Desktop/Limbic-master/input/segment/CNNSingularEmbedded/" + j + ".txt"
        with open(file_path, 'r', encoding='utf8') as f:
            content = f.read()
            content = content.replace('\n',' ')
        if i in neg_aspects_comments:
            neg_aspects_comments[i].append(content)
        else:
            neg_aspects_comments[i] = [content]

with open('/Users/shrey/Desktop/Limbic-master//outputapp/aspects.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Aspect", "Positive comments keywords", "Negative comments keywords"])
    for i in aspect:
        writer.writerow( [i, ' '.join(aspect[i][0]), ' '.join(aspect[i][1]) ])

    
with open('/Users/shrey/Desktop/Limbic-master//outputapp/aspectcommentgroup.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in pos_aspects_comments:
        writer.writerow([i, ' '.join(pos_aspects_comments[i]).replace("\n"," ") ] )
           

for i in aspect:
    with open('/Users/shrey/Desktop/Limbic-master//outputapp/comments_clustered_by_comments/' + str(i) + '.txt', 'w', newline='') as file:
        a = 'Keywords: ' + ' '.join(aspect[i][0]) + '\n\n'      
        b = '\n\n'.join(pos_aspects_comments[i]) + '\n\n'
        c = 'Keywords: ' + ' '.join(aspect[i][1]) + '\n\n'
        d = '\n\n '.join(neg_aspects_comments[i]) + '\n\n'
        file.write(a+b+c+d)
                 
        