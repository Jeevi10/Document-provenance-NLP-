#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 21:00:29 2017

@author: oem
"""

import numpy as np
import csv
import glob
from nltk.corpus import stopwords
from nltk import ngrams
import os
import threading
import time
from hashlib import md5
from nltk.corpus import stopwords

path = '/home/oem/Documents/GoogleNgram1/md51/'

def listFiles():
    files=[]
    for filename in sorted(os.listdir(path)):
        files.append(path+str(filename))
    return files



   
        
def Exponetionalsearch(a,x):
    bound=1;
    f=open(a)
    lines_list=f.read().split('\n')
    words=[]
    
    for line in lines_list:
        words.append(line.split('\t'))
        
    n=len(words)
    while(bound<n) and words[bound][0]<x:
        bound*=2;
    return binarySearchword(a,x,int(bound/2),min(bound,n))        

            
    
def binarySearchword(a, x,low,high):
    
    start_time=time.time()
    f=open(a)
    lo=low
    lines_list=f.read().split('\n')
    words=[]
    
    for line in lines_list:
        words.append(line.split('\t'))
        
    lines=len(words)
    print(lines)
#    if lo < 0:
#        raise ValueError('lo must be non-negative')
    if high is None:
        high = lines-1
    while lo < high:
        mid = (lo + high) >> 1
        if x== words[mid][0]:
            print((time.time() - start_time))
            print(x, words[mid][1])            
            return x,words[mid][1]
        else:
            if x < words[mid][0]:  # Change `<=' to `<', and you get bisect_right.
                high = mid
            else:
                lo = mid + 1
    print((time.time() - start_time))

    return x,0
            
    

           
    if words[0][0]> x:
      
        return words[0][0], 0
    else:
        return words[lines-2][0], lines-1



    
    
#def binarySearch(a, x, lo=0, hi=None):
#
#    f=open(a)
#    lo=0
#    lines_list=f.read().split('\n')
#    lines=len(lines_list)
#    if lo < 0:
#        raise ValueError('lo must be non-negative')
#    if hi is None:
#        hi = lines-1
#    while lo < hi:
#        mid = (lo + hi) >> 1
#        if x== lines_list[mid].split(' ', 1)[0]:
#            print("FOUND")
#            return x, mid
#        if x < lines_list[mid].split(' ', 1)[0]:  # Change `<=' to `<', and you get bisect_right.
#            hi = mid
#        else:
#            lo = mid + 1
#            

    
#lines_list[mid][:1]:
           
#    if lines_list[0].split(' ', 1)[0]> x:
#        print(lines_list[0].split(' ', 1)[0])
#        return lines_list[0].split(' ', 1)[0],0
#    else:
#        print(lines_list[lines-1].split(' ', 1)[0])
#        return lines_list[lines-1].split(' ', 1)[0], lines-1

            
        
#def findPosition(file_list, word):
#    lo=0
#    hi=len(file_list)
#    
#    while lo<hi:
#        mid=(lo+hi) >> 1
#        f=file_list[mid]
#        print(f)
#        char, line=binarySearch(f, word)
#        if word==char:
#            return mid, line
#            
#        if word<char:
#            hi=mid
#        else:
#            lo=mid+1
            
    
            
    
def docu(word,suspicious,source):
#    g=open(os.path.join("/home/oem/Desktop/test RA/test RA1/test1/", "shared"),'r')  
#    c=g.read()
#    c = ' '.join([word.lower() for word in c.split()])
#    h=stopwords.words('english')
#    n =1
#    sixgrams2= ngrams(c.split(), n)
#    wordlist2=[]
#    for grams in sixgrams2:
#            wordlist2.append(" ".join(grams))
#    words=[]        
#    for word in wordlist2:
#        if word not in h:
#            words.append(word)
#    del wordlist2
   
    words=word

    f=open(os.path.join(source),'r')  
    a=f.read()
    a = ' '.join([word.lower() for word in a.split()])
    n = 5
    sixgrams = ngrams(a.split(), n)
    wordlist=[]
    for grams in sixgrams:
        if len((set(grams)).intersection(set(words)))>=2:
                wordlist.append(" ".join(grams))



    g=open(os.path.join(suspicious),'r')  
    b=g.read()
    b = ' '.join([word.lower() for word in b.split()])
    n = 5
    sixgrams1= ngrams(b.split(), n)
    wordlist1=[]
    for grams in sixgrams1:
        if len((set(grams)).intersection(set(words)))>=2:
            wordlist1.append(" ".join(grams))
    #    for gram in grams:
    #        print(gram)
    #        if len((set(gram)).intersection(set(words)))>=1:
    #            
    sou=set(wordlist)
    sus=set(wordlist1)
    com=sou.intersection(sus)
    
    sou1=list(sou-com)
    sus2=list(sus-com)
    
    return sou1,sus2,com


#def splitingcorpusword(file): 
#    path=file
#    g1=open(os.path.join(path),'r')
#    lines_list=(g1.read().split('\n'))
#    words=[]
#    for line in lines_list:
#        words.append(line.split('\t'))
#    return words

#def findword(wordlist,words):
#    i=wordlist
#    for i2 in words:
#        if i==i2[0]:
#            print(i,i2[1])
#            return(i,i2[1])


def shared(suspicious,source):
    f=open(os.path.join(source),'r')  
    a=f.read()
    a = ' '.join([word.lower() for word in a.split()])
    
    g=open(os.path.join(suspicious),'r')  
    b=g.read()
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
    new=[]
    for m in l2:        
        l3.append(set(m))   
    if not l3:
        return False
    else:
        X=list(set.union(*l3))
        print(X)
        h=stopwords.words("english")
        for ele in X:
            if not ele in h:
                new.append(ele)
        print(new)
        return new
#        
            
              
def freq(file):
    
    path = '/home/oem/Documents/GoogleNgram1/md51/'    
    word_frequency=[]  
    suspisious=0    
    for i in range(len(file)):
        
        #mid,line=findPosition(dic,file[i].split(' ', 1)[0])
        word=file[i].split(' ', 1)[0]
        hash_md5 = md5(word.encode('utf8')).hexdigest()
        filename=path+str(hash_md5)+".txt"
        if os.path.isfile(filename):
            print(filename,word)
            sentence,frequency=Exponetionalsearch(filename,file[i])
            
            word_frequency.append((sentence,frequency))            
            suspisious+=int(frequency)
        else:
            word_frequency.append((file[i],0))
            
    if len(word_frequency)==0:
        print("nothing to compare")
        return 0,0
    else:    
        return word_frequency,suspisious/len(word_frequency)



def data():
    path='/home/oem/Downloads/pan13-text-alignment-training-corpus-2013-01-21/pairs'   
    accuracy=0
    counter=0
    lines = [line.rstrip('\n') for line in open(path, encoding="utf8")]
    avge=[]
    for line in lines:        
        suspicious=line.split(' ',1)[0]
        source=line.split(' ',1)[1]
        counter+=1
        sourcepath='/home/oem/Downloads/pan13-text-alignment-training-corpus-2013-01-21/src/'
        suspiciouspath='/home/oem/Downloads/pan13-text-alignment-training-corpus-2013-01-21/susp/'
        sourcefile=sourcepath+source
        suspiciousfile=suspiciouspath+suspicious
        shareds=shared(suspiciousfile,sourcefile)
        if shareds==False:
            print("cant classify")
            avge.append(["can't classify","can't classify"])
            
        
        else:
            sou,sus,com=docu(shareds,suspiciousfile,sourcefile)
    
            wordfrqsou,souavg=freq(sou)
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5"*4)
            wordfrqsus,susavg=freq(sus)
            avge.append([souavg,susavg])
            
            if souavg>=susavg:
                print(str(source)+' is original')       
                accuracy+=1
                print("counter",counter)
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5"*4)
                print('accuracy'+str(accuracy/counter))
          
            else:
                print(str(suspicious)+' is original')
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5"*4)
                print("counter",counter)
                print('accuracy'+str(accuracy/counter))
    
    return accuracy/counter,avge
        
            
#sourcepath='/home/oem/Downloads/pan13-text-alignment-training-corpus-2013-01-21/src/'
#suspiciouspath='/home/oem/Downloads/pan13-text-alignment-training-corpus-2013-01-21/susp/'
#suspicious,source=data()
#sourcefile=sourcepath+source
#suspiciousfile=suspiciouspath+suspicious
#sou,sus,com=docu(shared(suspiciousfile,sourcefile),suspiciousfile,sourcefile)
##dic=listFiles()
#wordfrqsou,souavg=freq(sou)
#print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
#wordfrqsus,susavg=freq(sus)
#
#if souavg>=susavg:
#    print('sou is original')
#    
#else:
#    print('sus is original')


#    mid,line=findPosition(listFiles(), grams()[i][0])
    
#        worfreq.append(binarySearchword(listFiles()[j],grams()[i]))
        
#    continue;
   
#    print(mid)

acc,avge=data()