#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:40:09 2018

@author: shrey
"""

from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost:9000')
sentence = "Some GENIUS engineer have decided that out of all the sounds on this planet!"
sentence2 = "good"
res = nlp.annotate(sentence2,
                   properties={
                       'annotators': 'sentiment',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })
for s in res["sentences"]:
    print("%d: '%s': %s %s" % (
        s["index"],
        " ".join([t["word"] for t in s["tokens"]]),
        s["sentimentValue"], s["sentiment"]))
    
#0-5 very negative to very postive