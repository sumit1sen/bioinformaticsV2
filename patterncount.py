__author__ = 'ssen'

def pattern_count(text, pattern):
    count = 0
    lenText = len(text)
    lenPattern = len(pattern)
    for i in range(0,lenText-lenPattern+1):
        if (text[i:i+lenPattern]==pattern):
            count=count+1
    return count


f=open('C:/dataset_2_6.txt')
s=f.read()
print(s)
c=pattern_count(s,'CATACCGCA')
#c = pattern_count('CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCTCTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACTCGCGCAGGTTGAGTA','CTC')
#print c
c = pattern_count('CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC', 'CGCG')
print(c)
