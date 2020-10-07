import math

def prob(n, p, r):
    '''
        p là xác suất có được mặt ngửa của 1 đồng xu
        r là số lần tung đồng xu được mặt ngửa
        n+r là số lần tung đồng xu để có r mặt ngửa
        n là số lần tung đồng xu được mặt sấp
        
    '''
    return math.comb(n+r-1,n)*((1-p)**n)*(p**r)

def inforMeasure(n, p, r):
    return -math.log2( prob(n, p, r) )

def sumProb(N, p, r):
    ans = 0
    for i in range(1,N+1):
        ans += prob(i, p, r)
    return ans

def approxEntropy(N, p,r):
    sum = 0
    for i in range(1,N+1):
        sum =+ prob(i, p, r) * inforMeasure(i, p, r)
    sum /= N
    return sum
    '''
    Khi N đủ lớn thì approxEntropy sẽ xấp xỉ với Entropy của nguồn tin negbinomial
    '''

'''
N=10
p=0.5
'''
print('Prob: ', prob(1,0.5, 1))
print('inforMeasure: ', inforMeasure(5,0.5, 3))
print('sumProb: ', sumProb(100,0.5,50))
print('approxEntropy: ', approxEntropy(10,0.5,3))
