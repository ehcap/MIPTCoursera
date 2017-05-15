import re
import numpy as np
from scipy.spatial.distance import cosine
filehandle = open('C:\AnacondaSrc\Course1week1\Week2\sentences.txt')
fullwordset = set()
filelines = list()
i = 0
for fileline in filehandle:
    filelines.insert(i,fileline)
    lwordlist = re.split('[^a-z]', fileline.lower())
    wordlist = [x for x in lwordlist if x != '']
    for word in wordlist:
        fullwordset.add(word)
    i = i + 1
filehandle.close()

# Create dict
t = list(fullwordset)
worddict = {x:t[x]  for x in range(len(t))}
print len(t)
print worddict

# Analyze filelines and construct matrix with word usage
wordusage = np.empty((0,len(worddict)))
res = np.empty(22)
i = 0
max1 = 0
max2 = 0
for fileline in filelines:
    lwordlist = re.split('[^a-z]', fileline.lower())
    wordlist = [x for x in lwordlist if x != '']
    t = [wordlist.count(worddict.get(x)) for x in range(len(worddict))]
    wordusageline = np.array([t])
    if i == 0 :
        sentence = wordusageline
    wordusage = np.concatenate((wordusage, wordusageline), axis=0)
    cos = cosine(sentence, wordusageline)
    print i, 'Cosine=', cos
    i = i + 1
    res = np.append(res,cosine)

print np.min(res)
print wordusage.shape







