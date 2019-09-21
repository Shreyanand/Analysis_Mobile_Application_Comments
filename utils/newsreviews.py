#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:06:36 2018

Extracts news apps, cleans, stems, and stores clean txt

@author: shrey
"""

import csv
import re
import nltk
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer





#appId = [1064216828,284862083,300255638,304158842,306621789,319740707,324906251,331786748,334256223,352509417,352969997,358801284,364147881,364387007,367623543,370614765,396885309,409128287,421216878,438875956,459182288,504631398,522921599,602660809,646100661,784982356,896628003,913753848]
#appId = [str(x) for x in appId]
#fi = open(location, 'r')
#data = fi.read()
#fi.close()
#fo = open(location, 'w')
#fo.write(data.replace('\x00', ''))
#fo.close()

#with open('/Users/shrey/Documents/appreview.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    data = [row for row in csv.reader(csvfile.read().splitlines())]
#with open('/Users/shrey/Documents/CNNnews.txt','w') as tfile:
#    for ele in data[1:]:
#        if len(ele) > 6 :
#            if ele[6] == '331786748':
#                s = ele[1] + " " + ele[2]
#                print(s,file=tfile)
                
docs = []
with open('/Users/shrey/AnacondaProjects/Application_reviews/Experiments/CNNnouns/RawData/CNNnews.txt','r') as tfile:
    for line in tfile:
        docs.append(line)

tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
en_stop.extend(['app','cnn','news'])
#p_stemmer = PorterStemmer()
lemma= WordNetLemmatizer()

texts = []

# loop through document list
for i in docs:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    tagged = nltk.pos_tag(stopped_tokens)
    nouns = [i[0] for i in tagged if i[1][0] == 'N']
    # stem tokens
    lemma_tokens = [lemma.lemmatize(i,pos='n') for i in nouns]
    
    lemma_sentences = ' '.join(lemma_tokens)
    
    # add tokens to list
    if len(lemma_tokens) > 1:
        texts.append(lemma_tokens)

sents = []
for sentence in texts:
    for word in sentence:
        if word  == 's':
            sentence.remove(word)
    s  =' '.join(sentence)
    sents.append(s)
            
with open('/Users/shrey/AnacondaProjects/Application_reviews/Experiments/CNNnouns/CleanedData/Lemmatizingdata.txt','w') as tfile:
    for ele in sents:
        print(ele,file=tfile)
        
#        
        
        
        
        
        
        
        
        
        
        
