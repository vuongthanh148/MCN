import math

def prob(n, p):
    return n+p

def inforMeasure(n, p):
    return -math.log2( prob(n, p) )

def sumProb(N, p):
    return 0

def approxEntropy(N, p):
    return 0


print(inforMeasure(2,0.5))

