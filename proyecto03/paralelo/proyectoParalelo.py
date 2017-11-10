#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpi4py import MPI
import string, os, time, sys, collections
from jaccardParalelo import*
from kmeansParalelo import*


STOPWORDS = ["a", "able", "about","1","2","3","4","5","6","7","8","9","0","above", "according", "accordingly", "across", "actually", "after", "afterwards", "again", "against", "all","mr","|", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "around", "as", "aside", "ask", "asking", "associated", "at", "available", "away", "awfully", "b", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "both", "brief", "but", "by", "c", "came", "can", "cannot", "cant", "cause", "causes", "certain", "certainly", "changes", "clearly", "co", "com", "come", "comes", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "course", "currently", "d", "definitely", "described", "despite", "did", "different", "do", "does", "doing", "done", "down", "downwards", "during", "e", "each", "edu", "eg", "eight", "either", "else", "elsewhere", "enough", "entirely", "especially", "et", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "f", "far", "few", "fifth", "first", "five", "followed", "following", "follows", "for", "former", "formerly", "forth", "four", "from", "further", "furthermore", "g", "get", "gets", "getting", "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "h", "had", "happens", "hardly", "has", "have", "having", "he", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "hi", "him", "himself", "his", "hither", "hopefully", "how", "howbeit", "however", "i", "ie", "if", "ignored", "immediate", "in", "inasmuch", "inc", "indeed", "indicate", "indicated", "indicates", "inner", "insofar", "instead", "into", "inward", "is", "it", "its", "itself", "j", "just", "k", "keep", "keeps", "kept", "know", "knows", "known", "l", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "like", "liked", "likely", "little", "ll", "look", "looking", "looks", "ltd", "m", "mainly", "many", "may", "maybe", "me", "mean", "meanwhile", "merely", "might", "more", "moreover", "most", "mostly", "much", "must", "my", "myself", "n", "name", "namely", "nd", "near", "nearly", "necessary", "need", "needs", "neither", "never", "nevertheless", "new", "next", "nine", "no", "nobody", "non", "none", "noone", "nor", "normally", "not", "nothing", "novel", "now", "nowhere", "o", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "only", "onto", "or", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "own", "p", "particular", "particularly", "per", "perhaps", "placed", "please", "plus", "possible", "presumably", "probably", "provides", "q", "que", "quite", "qv", "r", "rather", "rd", "re", "really", "reasonably", "regarding", "regardless", "regards", "relatively", "respectively", "right", "s", "said", "same", "saw", "say", "saying", "says", "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "she", "should", "since", "six", "so", "some", "somebody", "somehow", "someone", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify", "specifying", "still", "sub", "such", "sup", "sure", "t", "take", "taken", "tell", "tends", "th", "than", "thank", "thanks", "thanx", "that", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "theres", "thereupon", "these", "they", "think", "third", "this", "thorough", "thoroughly", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "twice", "two", "u", "un", "under", "unfortunately", "unless", "unlikely", "until", "unto", "up", "upon", "us", "use", "used", "useful", "uses", "using", "usually", "uucp", "v", "value", "various", "ve", "very", "via", "viz", "vs", "w", "want", "wants", "was", "way", "we", "welcome", "well", "went", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "willing", "wish", "with", "within", "without", "wonder", "would", "would", "x", "y", "yes", "yet", "you", "your", "yours", "yourself", "yourselves", "z", "zero"]

def leerArchivo():
    timeIni = time.time()
    global words, otroWords, arr, mapa
    words = []
    otroWords = []
    arr = []
    mapa = dict()
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size
    name = MPI.Get_processor_name()

    comm.bcast(words, 0)
    for filename in os.listdir(str(sys.argv[1])):
        if str(sys.argv[1]+filename).endswith(".txt"):
            content = open(str(sys.argv[1]+filename), 'r')
            txt = content.read().lower()
            words = txt.replace("\r\n", " ").replace("\t"," ").replace("\n"," ").replace("\r","").replace("{","").replace("}","").replace("=","").replace("$","").replace("!","").replace("-","").replace("[","").replace("]","").replace(".","").replace(",","").replace(":","").replace(";","").replace("_","").replace("*","").replace("+","").replace("'","").replace("?","").replace("¿","").split()
            #wordsUnir = comm.gather(words, 0)
            arr.append(words)

    arreglo = comm.bcast(arr)
    for i in range(rank,len(arr),size):
        for j in range(rank,len(arr[i]),size):
          if arreglo[i][j] not in STOPWORDS:
            #gather = comm.gather(arreglo[i][j], 0)
            otroWords.append(arreglo[i][j])
    #print otroWords, rank
    mapa = collections.Counter(otroWords).most_common(15)
    tMayu = dict(mapa).keys()
    #print tMayu, rank
    fdt = []
    if rank == 0:
        for doc in arr:
            result = []
            comm.bcast(result,0)

            for i in range(len(tMayu)):
                result.append(0)
            for word in doc:
                if word not in STOPWORDS:
                    if word in tMayu:
                        result[tMayu.index(word)] += 1
            #print(result), rank
            #print("-"*50)
            #gather = comm.gather(result, 0)
            fdt.append(result)
    #print fdt
    mat = np.empty((len(fdt),len(fdt)))
    for i in range(rank,len(fdt),size):
        for j in range(rank,len(fdt),size):
            mat[i][j] = 1-jaccard_similarity(fdt[i],fdt[j])
    comm.bcast(mat, 0)
    #jaccard(result)
    #print mat
    
    cents, C = kMeans(mat, 2)
    #print C
    #print "-"*50
    #print cents
    print(time.time() - timeIni)
    textos = os.listdir(str(sys.argv[1]))
    '''categoria1 = []
    categoria2 = []
    #print len(textos)-1
    comm.bcast(textos, 0)
    for i in range(len(textos)):
        if C[i] == 0:
                categoria1.append(textos[i])
        else:
                categoria2.append(textos[i])
    print "Cluster 1 : ", categoria1
    print "Cluster 2 : ", categoria2'''
    clusters={}
    for i in range(len(textos)):
        if C[i] in clusters:
            clusters[C[i]].append(textos[i])
        else:
                clusters[C[i]]=[textos[i]]
    for i in clusters:
        print ("Cluster "+str(i)+" ",clusters[i])
leerArchivo()
