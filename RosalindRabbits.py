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


def fibonacciDP(n,m):
    fib = [-1]*n
    fib[0] = 1
    fib[1] = 1

    fibTotal = 0
    for i in range(0,n):
        if (i>0):
            if fib[i-1] == -1:
                fib[i-1] = getFib(i-1);
            fibTotal += fib[i-1];
        if (i>1)

    young=[0]*n
    old = [0]*n
    young[0] = 1
    young[1] = 1
    for i in range(0,n):
        if (i<2)
print fibonacciDeath(5,3)

