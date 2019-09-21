#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:59:36 2018

@author: shrey
"""


import sys
import numpy as np
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from gensim import corpora, models
import gensim
import csv
import _pickle as cPickle
from sklearn.externals import joblib
from string import digits
import bz2
import pyLDAvis
import pyLDAvis.gensim

path = '/Users/shrey/AnacondaProjects/Application_reviews/Experiments/CNN/'
docs = []
with open(path + 'CleanedData/Lemmatizingdata.txt','r') as tfile:
    for line in tfile:
        docs.append(line)

tokenizer = RegexpTokenizer(r'\w+')
texts = []
for i in docs:
    tokens = tokenizer.tokenize(i)
    texts.append(tokens)
    
dictionary = corpora.Dictionary(texts) #returns 8989 unique tokens: ['disappointed', 'longer
corpus = [dictionary.doc2bow(sentence) for sentence in texts] #DTM Corpus is a list of [documents] sentences [ for each sentence: a list of frequency of each word in the sentence]


lda = gensim.models.ldamulticore.LdaMulticore(corpus, id2word=dictionary,num_topics=20, chunksize=1000, passes=20, workers=4)
#tokenscleanedCNN = open('/Users/shrey/AnacondaProjects/Application_reviews/Texts/tokens_after_lemmas_and_rm_stopwords.txt', 'w')
#for item in texts:
#    tokenscleanedCNN.write("%s\n" % item)   
    
dictionary.save_as_text(path + 'Dictionary/dictionary.txt')
corpora.MmCorpus.serialize(path + 'DTMcorpora/DTM.mm', corpus)   
joblib.dump(lda, path + 'LDAmodel/lda.pkl')


#dictionary = gensim.corpora.Dictionary.load_from_text('Texts/lemmas_nostopwords_with_otherdatacleaning_dictionary.txt')
#corpus = gensim.corpora.MmCorpus('Models/lemmas_nostopwords_corpus.mm')
#lda = joblib.load('Models/ldamodel.pkl')
##(lda.print_topics(num_topics=20, num_words=8))
#
#
#lda_vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
#pyLDAvis.display(lda_vis)