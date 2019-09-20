#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 20:48:43 2018

@author: shrey
"""
import requests
from bs4 import BeautifulSoup
import sys


try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
 
# to search
#query = "Russian hackers sent phishing emails to compromise North Carolina State University's backup servers." 
query = "Through a command-and-control HTTP response message sent to network administrator’s host, the malware begins to proxy TCP connections"
#query = "gun laws"
#for j in search(query, tld="co.in", num=1, stop=1, pause=2):
#    #f = requests.get(j)
#    print (j)


data = []
links = (i for i in search(query, tld="com", lang="en", num=150, start =0, stop=1, pause=2))

while len(data) < 100000:
    try:
        link = next(links)
        print(link)
        page = requests.get(link).text
        soup = BeautifulSoup(page, 'html.parser')
        paras = soup.find_all('p')
        text = ''.join(i.text for i in paras)
        if len(text) > 1000:
            data.append(text)
        print("Data Appened")
    except:
        print("Generator empty")
        break

with open('caltagirone.txt', 'w') as f:
    for i in data:
        f.write(i + "\n")
