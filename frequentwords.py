__author__ = 'ssen'

import patterncount

def frequentwords(text, k):
    frequentpatterns = []
    counts=[]
    lenText = len(text)
    for i in range(0,lenText-k):
        pattern = text[i:i+k]
        count = patterncount.pattern_count(text, pattern)
        counts.append(count)
    maxcount = max(counts)
    for i in range(0,lenText-k):
        if counts[i] == maxcount:
            frequentpatterns.append(text[i:i+k])

    return list(set(frequentpatterns))

f=open('C:/dataset_2_9.txt')
s=f.read()

fpatterns = frequentwords(s,13)
#print fpatterns
fpatterns = frequentwords('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA',3)
print fpatterns
