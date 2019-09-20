##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Wed Feb 21 16:20:27 2018
#
#@author: shrey
#"""
#
import numpy as np
import guidedlda
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE  
import pyLDAvis

path = '/Users/shrey/AnacondaProjects/Application_reviews/Experiments/CNN/'


docs = []
with open(path + 'CleanedData/Stemmingdata.txt','r') as tfile:
    for line in tfile:
        docs.append(line)
        


cvectorizer = CountVectorizer(min_df=5, stop_words='english')
X = cvectorizer.fit_transform(docs)
vocab = cvectorizer.get_feature_names()
word2id = dict((v, idx) for idx, v in enumerate(vocab))

with open(path + 'Dictionary/Vocabsklearn.txt','w') as tfile:
    for ele in vocab:
        print(ele,file=tfile)
        

#print(X.shape)
#print (vocab)
#print(X.sum())
# Normal LDA without seeding

seed_topic_list = [['ui','interfac','visual','look','format', 'chang', 'layout','design','intuit'],
                   ['qualiti','stabl','stabil','speed','memori','crash','freez','bug'],
                   ['ad','commerci','advertis','paid','free']
                  ]
        

model = guidedlda.GuidedLDA(n_topics=3, n_iter=1000, random_state=7, refresh=20)

seed_topics = {}
for t_id, st in enumerate(seed_topic_list):
    for word in st:
        seed_topics[word2id[word]] = t_id

X_topics = model.fit_transform(X, seed_topics=seed_topics, seed_confidence=0.15)


n_top_words = 10
topic_word = model.topic_word_
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))

_lda_keys = []
for i in range(X_topics.shape[0]):
    _lda_keys.append(X_topics[i].argmax())
    
#    
#       
#tsne_model = TSNE(n_components=2, verbose=1, random_state=0, angle=.99, init='pca')
#tsne_lda = tsne_model.fit_transform(X_topics)
##
#with open (path + 'TSNEmodel/Gldatsne.mo','wb') as f:
#    pickle.dump(tsne_lda,f)

with open (path + 'TSNEmodel/Gldatsne.mo','rb') as f:
    tsne_lda = pickle.load(f)

color = []
UI = []
Quality = []
Ads = []

for c,i in enumerate(_lda_keys):
    if i == 0:
        color.append("red")
        UI.append(docs[c])
    elif i == 1:
        color.append("blue")
        Quality.append(docs[c])
    else:
        color.append("green")
        Ads.append(docs[c])
        
fig,ax = plt.subplots()
sc = plt.scatter(tsne_lda[:, 0], tsne_lda[:, 1], c=color,s=2)
      
annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}".format(" ".join([docs[n] for n in ind["ind"]]))
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor("red")
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)
plt.title("Red: UI; Blue: Quality; Green: Advertisement")
plt.show()

