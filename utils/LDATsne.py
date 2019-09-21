#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:33:20 2018

@author: shrey
"""


import numpy as np
from gensim import corpora, models
import gensim
import csv
import _pickle as cPickle
from sklearn.externals import joblib
import bz2
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from scipy import stats

# a t-SNE model
# angle value close to 1 means sacrificing accuracy for speed
# pca initializtion usually leads to better results 

 

path = '/Users/shrey/AnacondaProjects/Application_reviews/Experiments/CNN/'
dictionary = gensim.corpora.Dictionary.load_from_text(path + 'Dictionary/dictionary.txt')
corpus = gensim.corpora.MmCorpus(path + 'DTMcorpora/DTM.mm')
lda = joblib.load(path + 'LDAmodel/lda.pkl')
print (len(corpus))

color = []
for corpus_line in corpus[:10000]:
    sorted_topic_line = list(sorted(lda[corpus_line], key=lambda x: x[1], reverse=True))
    color.append(sorted_topic_line[0][0])
    
    
lda_output = []
for line in corpus[:10000]:
    lda_output.append(lda[line])
    
topics_data = np.zeros(shape=(10000,50))

for i, line in enumerate(lda_output):
    for topic_line in line:
            topics_data[i][topic_line[0]] = topic_line[1]
            
topics_data_norm  = stats.zscore(topics_data, axis=0)           
tsne_model = TSNE(n_components=2, verbose=1, random_state=0, angle=.99, init='pca')

# 20-D -> 2-D
tsne_lda = tsne_model.fit_transform(topics_data_norm )
print (tsne_lda)