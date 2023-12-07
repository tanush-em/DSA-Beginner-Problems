# PRINT 1 TO N WITHOUT USING LOOPS

def printnum(n,i):
    if i > n:
        return
    print(i)
    i = i + 1
    printnum(n,i)
  
n = 10 
i = 1 
printnum(n,i)