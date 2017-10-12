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

# files = []
# for i in os.listdir("/home/ana/clusteringDocumentos/serial"):
#     if i.endswith('.txt'):
#         files.append(open(i))
# print i

def leerArchivo():
      for i in range(1,len(sys.argv)):
        print(i)
        fread = open(str(sys.argv[i]),'r')
        txt = fread.read()
        print txt.replace("\r\n", "").replace("\t"," ").split()
leerArchivo();
