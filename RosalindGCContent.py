__author__ = 'ssen'

def countGCInString(dnaString):
    dnaString = dnaString.upper()
    gcCount = 0
    for c in dnaString:
        if c == 'C' or c == 'G':
            gcCount +=1

    return gcCount*100.0/(len(dnaString)*1.0)

def countGC(filename):
    file = open(filename)
    fastaLine = file.readline()
    fname = fastaLine[1:len(fastaLine)-1]
    fastaLine = file.readline()
    maxFilename = ""
    maxFraction = 0
    while fastaLine != "":
        dnaString = ""
        # print fname
        while fastaLine != "" and fastaLine[0] != '>':
            dnaString += fastaLine.rstrip('\n')
            fastaLine = file.readline()
        gcFraction = countGCInString(dnaString)
        if gcFraction > maxFraction:
            maxFraction = gcFraction
            maxFilename = fname

        fname = fastaLine[1:len(fastaLine)-1]
        fastaLine = file.readline()

    print maxFilename
    print maxFraction
countGC('C:\\rosalind_gc.txt')