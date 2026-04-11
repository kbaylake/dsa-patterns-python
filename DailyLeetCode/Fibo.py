'''def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    #0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    return fibo(n-1)+fibo(n-2)'''

## Overlapping Subproblem
'''def fibo(n):
    dc={}
    def backtrack(n):
        if n==0:
            return 0
        if n==1:
            return 1
        if n not in dc:
            curr=backtrack(n-1)+backtrack(n-2)
            dc[n]=curr
        curr=dc[n] 
        return curr
    return backtrack(n)'''
## Without Recursion
def fibo(n):
    a=0
    b=1
    if n==0:
        return 0
    if n==1:
        return 1
    for i in range(n):
        tmp=b
        b=a+b
        a=tmp
    return a
print(fibo(6))