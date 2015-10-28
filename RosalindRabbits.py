__author__ = 'ssen'
import sys
def fibonacci(n, k):
    if (n<=2):
        return 1
    retVal = fibonacci(n-1,k) + k*fibonacci(n-2,k)
    return retVal

def fibonacciDeathV2Loop(n, m, born, mature, dying):

    if n==0:
        born[0] = 1
        x = []
        for i in range(m-1):
            x.append(long(0))
        mature[0]=x
        dying[0]=long(0)
        return long(1)
    matureTotal = long(0)
    for i in range(m-1):
        matureTotal += mature[n-1][i]
    matureTotal += dying[n-1]
    born.append(matureTotal)
    x = [long(0)]
    x[0]=born[n-1]
    for i in range(1,m-1):
        x.append(mature[n-1][i-1])
    mature.append(x)
    dying.append(mature[n-1][m-2])

    total = long(0)
    for i in range(m-1):
        total += mature[n][i]
    total += dying[n] + born[n]
    return total

def fibonacciDeathV2(n,m):

    n = n-1
    m=m-1
    born = [long(0)]
    mature = [[]]
    dying = [long(0)]
    retval = long(0)
    for i in range(n+1):
        retval = fibonacciDeathV2Loop(i,m,born, mature, dying)
        print retval

    print
    return retval

print fibonacciDeathV2(89,17)

