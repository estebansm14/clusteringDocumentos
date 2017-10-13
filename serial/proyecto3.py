# -*- coding: utf-8 -*-
import string, os, sys

STOPWORDS = ['a','able','about','across','after','all','almost','also','am','among',
             'an','and','any','are','as','at','be','because','been','but','by','can',
             'cannot','could','dear','did','do','does','either','else','ever','every',
             'for','from','get','got','had','has','have','he','her','hers','him','his',
             'how','however','i','if','in','into','is','it','its','just','least','let',
             'like','likely','may','me','might','most','must','my','neither','no','nor',
           'not','of','off','often','on','only','or','other','our','own','rather','said',
             'say','says','she','should','since','so','some','than','that','the','their',
             'them','then','there','these','they','this','tis','to','too','twas','us',
             'wants','was','we','were','what','when','where','which','while','who',
             'whom','why','will','with','would','yet','you','your']

def leerArchivo():
      words = ""
      for filename in os.listdir(str(sys.argv[1])):
          if str(sys.argv[1]+filename).endswith(".txt"):
                content = open(str(sys.argv[1]+filename), 'r')
                txt = content.read().lower()
                #print txt.replace("\r\n", "").replace("\t"," ").replace("-","").split()
                words = txt.replace("\r\n", "").replace("\t"," ").replace("-","").replace("[","").replace("]","").replace(".","").replace(",","").replace(":","").replace(";","").replace("_","").replace("*","").replace("+","").replace("'","").replace("?","").replace("¿","").split()
                #print words
      for i in words:
        for comparar in STOPWORDS:
          if str(comparar) == str(i) :
            words.remove(i)
      print words

leerArchivo()


