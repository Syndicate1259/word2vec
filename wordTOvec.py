# -*- coding: utf-8 -*-
"""
@author: Jose Sanchez (jose.sanchez849@gmail.com)
****************************************************************************************************************
*  -This is rev 2 of Dr. Tillquist (rctillquist20) w2vAnalogyTests.py. Thanks to CSU, Chico's organization     *
*CSC2 for sponsoring the research! The code was updated from Gensim 3.x to Gensim 4                            *
*(there was some function deprecation and other important changes to us) along with other improvements to code *
* https://github.com/RaRe-Technologies/gensim/wiki/Migrating-from-Gensim-3.x-to-4                              *
*                                                                                                              *
*  -Input is hardcoded in main with some changes needed for functions for file saving. This is one             *
*area of improvement, we can incorporate input from stdin and pass data to functions if needed)                *
*                                                                                                              *
*  -If-conditions can be used for the optional write and load hist functions for easier functionality. Better  *
* debugging if needed.                                                                                         *
*                                                                                                              *
****************************************************************************************************************
"""
import gensim
import gensim.downloader as api
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
from itertools import repeat
import json
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import wordnet
import random

#_______________CHECKERS________________________
def isfloat(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False
    
def isunderVocab(arg):
    for char in arg:
        if not(char.isalpha() and '_' in arg):
            if not(char == '_'):
                return False
    return True

def iswordVocab(arg):
    if not(arg.isalpha()):
        return False
    return True

def ismodelVocab(arg):
    return True

def checkResults(results):
    CORRECT=[]
    FAILED=[]
    DNE=[]
    dne=0                                           #Keeps track of words that dne.
    failed=0                                        #Keeps track of analogies field.
    correct=0                                       #Keeps track of correct analogies.
    
    for ((a,b,c,d), nearby, boole, dist) in results:
        if not(a in model.index_to_key):
            if a not in DNE:
                DNE.append(a)
        if not(b in model.index_to_key):
            if b not in DNE:
                DNE.append(b)
        if not(c in model.index_to_key):
            if c not in DNE:
                DNE.append(c)
        if not(d in model.index_to_key):
            if d not in DNE:
                DNE.append(d)
        if nearby[0][0] == d:
             CORRECT.extend([a,b,c,d,nearby[0][1]])
        else:
             temp=nearby[0][0]
             FAILED.extend([a,b,c,d,temp,nearby[0][1]])                 
        if dist == -99:
             dne+=1
        elif boole==False and dist != -99:
             failed+=1
        else:
             correct+=1
    return(CORRECT, FAILED, DNE, correct, failed, dne)

#_______________CHECKERS END________________________


#_______________HISTOGRAMS________________________
def loadFailedDistHist(file):
    file+='_Failed_synant'                      # UPDATE file NAME
    density=False                               # UPDATE DENSITY AS NEEDED
    save=True                                   # CHANGE TO FALSE TO NOT SAVE HISTOGRAMS 60-61
# TO EXTRACT THE DATA FROM THE TXT FILE
    my_file = open(file+'.txt', "r")
    content = my_file.read()
    my_file.close()
    content_list = content.split(",")
    sims = [float(items) for items in content_list if isfloat(items)]
# TO EXTRACT THE DATA FROM THE TXT FILE
    plt.hist(sims, density=False, bins=50, alpha=0.3, label='incorrect_synant '+FILE)
    plt.xlabel('Similarity (most_similar())')
    plt.ylabel('Density' if density else 'Count')
    plt.legend(loc='upper right')
    if save:
        plt.savefig(fname=file+'.png', bbox_inches='tight')
        
def loadCorrectDistHist(file):
    file+='_Correct_synant'                                         # UPDATE file NAME
    density=False                                                   # UPDATE DENSITY AS NEEDED
    save=True                                                       # CHANGE TO FALSE TO NOT SAVE HISTOGRAMS 86-87
# TO EXTRACT THE DATA FROM THE TXT FILE
    my_file = open(file+'.txt', "r")
    content = my_file.read()
    my_file.close()
    content_list = content.split(",")
# TO EXTRACT THE DATA FROM THE TXT FILE
    sims = [float(items) for items in content_list if isfloat(items)]
    plt.hist(sims, density=False, bins=50, alpha=0.3, label='correct_synant '+ FILE)# UPDATE LABEL TOO
    plt.xlabel('Similarity (most_similar())')
    plt.ylabel('Density' if density else 'Count')
    plt.legend(loc='upper right') 
    if save:                                                                #
        plt.savefig(fname=file+'.png', facecolor='r', bbox_inches='tight')  #
   
def loadRandomDistHist(file):
    file+='_Random'                                                # UPDATE file NAME
    density=False                                                  # UPDATE DENSITY AS NEEDED
    save=True                                                      # CHANGE TO FALSE TO NOT SAVE HISTOGRAMS 111-112
# TO EXTRACT THE DATA FROM THE TXT FILE
    my_file = open(file+'.txt', "r")
    content = my_file.read()
    my_file.close()
    content_list = content.split(".")
    content_list = '.'.join(content_list[1:])
    #print(content_list)
    L = json.loads(content_list)
    #print(L)
    sims = [items[4] for items in L if items[5]==0]
# TO EXTRACT THE DATA FROM THE TXT FILE
    plt.hist(sims, density=False, bins=50, alpha=0.3, label='random '+FILE)#UPDATE LABEL TOO
    plt.xlabel('Similarity (most_similar())')
    plt.ylabel('Density' if density else 'Count')
    plt.legend(loc='upper right')
    plt.show()                                                              
    if save:                                                                #
        plt.savefig(fname=file+'.png', facecolor='r', bbox_inches='tight')  #
#_______________HISTOGRAMS END________________________


#-------------------------WRITING FILES---------------------------------------
def writeFailedInfo(tfailed, file, vocab):
    file+='_Failed_synant.txt'                               # UPDATE NAME
    t = open(file, 'w')
    t.write("There were %s analogies that failed at getting the correct answer."%(tfailed))
    t.close()
    json.dump(vocab, open(file, 'a'))
        
def writeDNEInfo(tdne, file, vocab):
    file+='_Dne_synant.txt'                                  # UPDATE NAME
    t = open(file, 'w')
    t.write("There were %s analogies that weren't recognized by the model."%(tdne))
    t.close()
    json.dump(vocab, open(file, 'a'))

def writeCorrectInfo(tcorrect, file, vocab):
    file+='_Correct_synant.txt'                              # UPDATE NAME
    t = open(file, 'w')
    t.write("There were %s correct analogies."%(tcorrect))
    t.close()
    json.dump(vocab, open(file, 'a'))

def writeRandomInfo(trand, file, vocab):
    file+='_Random.txt'                                      # UPDATE NAME
    t = open(file, 'w')
    t.write("There are %s random analogies."%(trand))
    t.close()
    json.dump(vocab, open(file, 'a'))
    
def writeSynant(sym,ant,file):
    f = file + '_Synonyms'                               
    t = open(f, 'w')
    t.write("These are synonyms")
    t.close()
    json.dump(sym, open(f, 'a'))
    f = file + '_Antonyms'                                  
    t = open(f, 'a')
    t.write("These are antonyms")
    t.close()
    json.dump(ant, open(f, 'a'))
    
#-------------------------WRITING FILES END-----------------------------------

def collectAnalogies(analogy_file):
    A=[]
    with open(analogy_file, 'r')as f:
        for count, line in enumerate(f):                                #for line in f
            l = line.strip()
            if l[0] !=':' : A.append(l.split(' '))
    return A

#-------------------------ANALOGY --------------------------------------------
def analogysimilarities(analogy_file, nNearest=1, procs=1):
    jobs = collectAnalogies(analogy_file=analogy_file)
    results = []
    for job in zip(jobs, repeat(nNearest)):
        results.append(analogyTest(job))    
    results.sort(key=lambda x: x[1][0][1], reverse=True)                #sort by nearest (most similar) result of the analogy test
    return results

def analogyTest(args):
    ((a,b,c,d), n) = args
    if not( a in model.index_to_key and b in model.index_to_key and c in model.index_to_key and d in model.index_to_key): #This is for analogies not recognized by the model
        return ((a, b, c, d), [("<NONE>", -99)] , False, -99)
    nearby = model.most_similar(positive=[b,c], negative=[a], topn=n)   #a is to b as c is to what? b-a+c=?
                                                                        #print("After nearby")          #Used to make sure error was data not available from model
    #the following code computes the cosine similarity between b-a+c and d using the approach in
    #https://github.com/RaRe-Technologies/gensim/blob/develop/gensim/models/keyedvectors.py#L485
    w, x, y, z = model[a], model[b], model[c], model[d]
    sim = x/np.linalg.norm(x) - w/np.linalg.norm(w) + y/np.linalg.norm(y)
    sim = np.dot(z, sim) / (np.linalg.norm(z)*np.linalg.norm(sim))
    #print(a, b, c, d) #Debugging
    return ((a, b, c, d), nearby, nearby[0][0]==d, sim)     
#-------------------------ANALOGY END-----------------------------------

def loadW2V(w2vFile):
    return gensim.models.KeyedVectors.load_word2vec_format(w2vFile, binary=True if ('bin' in w2vFile.split('.')) else False)

def gloveFromW2V(gloveFile, save=''):
    w2vFile = '/'.join(gloveFile.split('/')[:-1]) + 'w2v_'+gloveFile.split('/')[-1]
    glove2word2vec(gloveFile, w2vFile if not save else save)
    return loadW2V(w2vFile)

#-------------------------Word Testing options-----------------------------------

def randomTriples(vocab):
    n=5                                                                 #Top n results and copy of n
    nn=5                                                              
    x=1
    place=0                                                              #x is the iterator and place is the placeholder
    r=random.sample(range(0,len(vocab)), 3)
    a=vocab[r[0]]
    b=vocab[r[1]]
    c=vocab[r[2]]
    nearby = model.most_similar(positive=[b,c], negative=[a], topn=n)   #a is to b as c is to what? b-a+c=?
    while place != n:
        if x+1 == nn :
            nn*=2
            nearby = model.wv.most_similar(positive=[b,c], negative=[a], topn=nn)   #a is to b as c is to what? b-a+c=?
        elif ismodelVocab(nearby[x][0]):
            d=nearby[x][0]    
            dist=nearby[x][1]
            print(a,b,c,d)
            RANDOM.append([a,b,c,d,dist,place])
            place+=1
            x+=1
        else:
            x+=1       
    return(RANDOM)

def returnfirstX(arg):
    WORDS=[]
    counter=0
    for word in model.key_to_index:
        if iswordVocab(word) and counter != arg:
            WORDS.append(word)
            counter+=1
        elif counter == arg:
            break
    return WORDS

def synant(vocab):
    synonyms=[]
    antonyms=[]
    for item in vocab:
        for syn in wordnet.synsets(item):
            for l in syn.lemmas():
                synonyms.append(item,l.name())
                if l.antonyms():
                    antonyms.append(item,l.antonyms()[0].name())
    return (synonyms,antonyms)
#-------------------------Word Testing options-----------------------------------

if __name__ == "__main__":
    DNE=[]                                  #DNE holds all words that weren't in the "Vocabulary"
    FAILED=[]                               #Failed holds all the analogies that failed
    CORRECT=[]                              #Correct holds all the analogies that are correct
    RANDOM=[]                               #Random holds random triples
    MODELVOCAB=[]                           #Modelvocab holds the model vocabulary
    WORDVOCAB=[]                            #Wordvocab holds all strings
    UNDERVOCAB=[]                           #Undervocab holds letters with underscores
    rand=20000                              #Number of random triples
    first=1000                              #Run for first x. Used so running model doesnt take forever
    
    # FILE='word2vec-google-news-300'
    FILE='GoogleNews-300.model'                                                           #New .model file
    # analogy_file="questions-words.txt"      
    analogy_file="questions-words2.txt"  #File used for testing model. I believe  
    
    if True: #Do we need the model for the current run? Changing to False saves time for some testing/generating figures
        print('Load model begin')
        # model = api.load(FILE)     
        model = gensim.models.KeyedVectors.load(FILE)                                     #For using new .model file. Given by Tillquist?
        print('Load model complete')
        for index, word in enumerate(model.index_to_key):
            MODELVOCAB.append(word)
            #print(f"word #{index}/{len(wv.index_to_key)} is {word}")

    print('Generate vocab')
    results = analogysimilarities(analogy_file)
    print('Generated vocab')
    
    info = checkResults(results)
    CORRECT, FAILED, DNE, correct, failed, dne = info
    # WORDVOCAB = [word for word in model.index_to_key if iswordVocab(word)]   #Replace is___vocab & ____VOCAB with desired vocab detection   #print("Before nearby")
    # if len(WORDVOCAB)> 2:                           #Make sure vocab is populated with at least 3 items. Replace with desired vocab
    #     for x in range(0,rand):
    #         print(x)#To show progress
    #         RANDOM = randomTriples(WORDVOCAB)       #Replace ____VOCAB func_var with desired vocab. WHY DOES THIS NOT OVERWRITE!? Confusion
    # FIRSK = returnfirstX()
    # SYNONYMS,ANTONYMS= synant(FIRSTK)               #Jose reporting in 09/08/22 10:02 am, seems like maybe missing removing the T would have helped
#---------------------------WRITING----------------------------------
    if '.' in FILE:
        FILE = FILE.split('.')
        FILE = FILE[:1]
        FILE = str(FILE)
    trash = input('Starting at line 117 are the write functions, make sure you update the file name in the function! Press ENTER to continue or CTRL+C to stop')# Never comment out this line, you will eventually accidentally overwrite files and forget
    writeFailedInfo(failed,FILE,FAILED)
    writeCorrectInfo(correct,FILE,CORRECT)
    writeDNEInfo(dne,FILE,DNE)
    # writeRandomInfo(rand,FILE,RANDOM)
    # writeSynant(SYNONYMS, ANTONYMS)
#---------------------------WRITING END----------------------------------
    trash = input('Starting at line 47 are the load histogram functions, make sure you update the file name in the function! Press ENTER to continue or CTRL+C to stop')# Never comment out this line

    # loadFailedDistHist(FILE)
    # loadCorrectDistHist(FILE)
    # loadRandomDistHist(FILE)

