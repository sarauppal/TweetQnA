# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:02:16 2019

@author: monst
"""


import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
set(stopwords.words('english'))

def preprocess(text):
   
        #remove everything after time stamp
        text = re.sub(r'((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]) ?(-) ([\s\S]+))', '', text)
        #remove @mentions with user ID
#        text = re.sub(r'@[A-Za-z0-9]+','',text)
        # Check characters to see if they are in punctuation
#        text = re.sub('\d+','', text)
        #remove user name
        text = re.sub(r'—.*?\(', '  ', text)
       #remove punctuation
        punctuations = '''!()-[]{};:'"\,<>./?#$%^&*_~'''
        nopunc = [char for char in text if char not in punctuations]
        # Join the characters again to form the string.
        combined = ''.join(nopunc)
        
        # convert text to lower-case
        combined = combined.lower()
        # remove URLs
        combined = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))', '', combined)
    
        
        # remove # but keep the hastag as word
        combined = re.sub(r'#([^\s]+)', r'\1', combined)
        # deEmojify
        combined = combined.encode('ascii', 'ignore').decode('ascii')
                          
                                  
     
        return combined