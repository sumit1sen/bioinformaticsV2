__author__ = 'ssen'
def fibonacci(n, k):
    if (n<=2):
        return 1
    retVal = fibonacci(n-1,k) + k*fibonacci(n-2,k)
    return retVal

def fibonacciDeath(n,m):
    if n<=0:
        return 0
    elif n<=2:
        return 1

    retVal = fibonacciDeath(n-3,m)
    retVal += fibonacciDeath(n-4,m)
    # retVal = retVal - fibonacciDeath(n-m-1,m)
    return retVal
print fibonacciDeath(5,3)
