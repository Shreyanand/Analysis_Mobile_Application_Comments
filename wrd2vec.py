#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:57:59 2018

@author: shrey
"""


from gensim.models import doc2vec
from sklearn.decomposition import PCA
import gensim
#import theano
#import theano.tensor as T
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import sys
import csv
import pickle
from sklearn.manifold import TSNE
from scipy import stats
            
        
#document = doc2vec.TaggedLineDocument('/Users/shrey/Documents/news.txt')

#lines = []
#with open('/Users/shrey/Documents/a2.txt','r') as tfile:
#    for line in tfile:
#        line  = line.replace("\n","")
#        lines.append([line])


#model = doc2vec.Doc2Vec(document, size = 200, window=8, min_count=5, workers=4)
#t  = stats.zscore(model.docvecs.doctag_syn0, axis=0)
#tsne_model = TSNE(n_components=2, verbose=1, random_state=0, angle=.99, init='pca')


#model.docvecs.most_similar("10")
#model.wv.similarity("fantacstic","great")
#words = list(model.wv.vocab)
#print(words)

#model.wv.most_similar(positive = ["speed"], topn=100)
#model.wv.most_similar(positive = ["UI"], topn=100)
#model.wv.most_similar(positive = ["privacy"], topn=100)
#model.wv.most_similar(positive = ["Memory"], topn=100)

### JUST PCA ####
#pca = PCA(n_components=2)
#result = pca.fit_transform(model.docvecs.doctag_syn0)
#print (len(result))


############ PLOT ##############################
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(result[:, 0], result[:, 1],result[:, 2], s=1)
##words = list(model.wv.vocab)


#for i, line in enumerate(lines):
#	plt.annotate(lines.index(line), xy=(result[i, 0], result[i, 1]))
with open ('/Users/shrey/Desktop/d2vtsne.mo','rb') as f:
    tsne_lda = pickle.load(f) 
plt.figure(num=None, figsize=(20, 12), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(tsne_lda[:, 0], tsne_lda[:, 1], s=1)
plt.show()
