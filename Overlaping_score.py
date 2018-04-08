#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:52:35 2017

@author: oem
"""

import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
import numpy as np
from nltk import ngrams
#%%

def shared(suspicious,source):
    f=open(os.path.join(source),'r')  
    a=f.read()
    a = re.sub("[^a-zA-Z]"," ",a )
    a = ' '.join([word.lower() for word in a.split()])
    
    g=open(os.path.join(suspicious),'r')  
    b=g.read()
    b = re.sub("[^a-zA-Z]"," ",b )
    b = ' '.join([word.lower() for word in b.split()])
    shared=[]
    i=20
    while i >2:
        n=i
        
        sixgrams1= ngrams(b.split(), n)
        sixgrams = ngrams(a.split(), n)
        sou=set(sixgrams)
        sus=set(sixgrams1)
        com=list(sus.intersection(sou))
        if not com:        
                
                i=i-1
        else:
            if not shared:
                for j in range(len(com)):
                    shared.append(com[j])     
                
                i=i-1
                
            else:            
                 for grams in com:
                     shared.append(grams)                 
                 i =i-1
            
    l2=shared[:]        
    for m in shared:
        for n in shared:
            if set(m).issubset(set(n)) and m != n:
                l2.remove(m)
                
                break
    
    l3=[]
    for m in l2:        
        l3.append(set(m))   
    if not l3:
        return False
    else:
        return l2


#%%




 
def removesharedpart(share,temp):
        sei=' '.join(share)     
           
        temp=(re.sub(sei,"",temp))
        
        return temp
                
                
        
        
        



#%%

def tok(doc):
    
    
    b=sent_tokenize(doc)
    new=[]
    for i in range(0,len(b)):
        letters_only = re.sub("[^a-zA-Z]"," ",b[i] ) 
    
        lower_case = letters_only.lower()        # Convert to lower case
        words = lower_case.split()               # Split into words
    
        h=stopwords.words("english")
    
        words = [w for w in words if not w in h]
        new.append(words)
    
    all_words=[]   
    for i in range(0,len(new)):
        all_words.append(nltk.FreqDist(new[i]))
        
    modi=[]
    for i in range(0,len(all_words)):
        modi.append(all_words[i].most_common(10))
        
    return new,modi
    
    
def tokshare(sharedpart):
    c=[]
    new1=[]
    for sen in sharedpart:
        sent=' '.join(sen)
        c.append(sent)
        
    for i in range(0,len(c)):
        letters_only1 = re.sub("[^a-zA-Z]"," ",c[i] ) 
    
        lower_case1 = letters_only1.lower()        # Convert to lower case
        words = lower_case1.split()               # Split into words
    
        h=stopwords.words("english")
    
        words1 = [w for w in words if not w in h]
        new1.append(words1)
    
    all_words1=[]   
    for i in range(0,len(new1)):
        all_words1.append(nltk.FreqDist(new1[i]))
        
        
    sharmodi=[]
    for i in range(0,len(all_words1)):
        sharmodi.append(all_words1[i].most_common(10))
        
    return sharmodi
    
    

        
    
#%%




def score(doc,sha):
    f=open(os.path.join(doc),'r')
    a=f.read()
    a=a.lower()
    global temp 
    temp=a
    
    for se in sha:
        temp=removesharedpart(se,temp)
        purepart=(removesharedpart(se,temp))
        
    new,modi=tok(purepart)    
    sharmodi=tokshare(sha)    
    inter=[]  
    
    for i in range(0,len(new)):
        for j in range(0,len(sharmodi)):
            inter.append (list(set(sharmodi[j]).intersection(set(modi[i]))))
     
    su=0    
    for se in inter:
        if not se:
            continue
            
        else:
            su+=len(se)
        
    score=(su/len(new))
    return score

    
def data(): 
    
    path='/home/oem/Downloads/pan13-text-alignment-training-corpus-2013-01-21/pairs'   
    accuracy=0
    counter=0
    lines = [line.rstrip('\n') for line in open(path, encoding="utf8")]
    scores=[]
    for line in lines:        
        suspicious=line.split(' ',1)[0]
        source=line.split(' ',1)[1]
        counter+=1
        sourcepath='/home/oem/Downloads/pan13-text-alignment-training-corpus-2013-01-21/src/'
        suspiciouspath='/home/oem/Downloads/pan13-text-alignment-training-corpus-2013-01-21/susp/'
        sourcefile=sourcepath+source
        suspiciousfile=suspiciouspath+suspicious
        share=shared(suspiciousfile,sourcefile)
        
        if share ==False:
            print("Nothing to  compare")
            scores.append(["no share part","no share part"])
        else:
            
            source_score=score(sourcefile,share)
            suspicious_score=score(suspiciousfile,share)
            print(source_score,suspicious_score)
            scores.append([source_score,suspicious_score])
            if source_score==suspicious_score:
                print("source doc or suspicious is original")
                print("counter"+str(counter))
                accuracy+=0.5
                print("accuracy"+str(accuracy/counter))
            if source_score>suspicious_score:
                print("source doc or suspicious is original")
                print("counter"+str(counter))
                accuracy+=1
                print("accuracy"+str(accuracy/counter))
            else:
                print("suspicious doc is oringinal")
                print("counter"+str(counter))
                print("accuracy"+str(accuracy/counter))
                
            
    return scores,accuracy/counter
                
            
            
            
scor,accuracy=data()            
            
            
            