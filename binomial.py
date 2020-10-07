import math

def prob(n, p, N):
    '''
        p là xác suất có được mặt ngửa của 1 đồng xu
        n là số đồng xu có mặt ngửa
        N là số đông xu được tung
    '''
    return math.comb(N,n)*((1-p)**(N-n))*(p**n)

def inforMeasure(n, p, N):
    return -math.log2( prob(n, p, N) )

def sumProb(N, p):
    ans = 0
    for i in range(1,N+1):
        ans += prob(i, p, N)
    return ans
    '''
        Ta có tổng xác suất các symbols:
            ans = NC0*(1-p)^N-0 * p^0 + NC1*(1-p)^N-1 * p^1 + NC2*(1-p)^N-2 * p^2 + ... + NCn(1-p)^N-n * p^n
            ans = ((1-p) + p)^N = 1^N = 1 (Khai triển nhị thức Newton)
    '''

def approxEntropy(N, p):
    sum = 0
    for i in range(1,N+1):
        sum =+ prob(i, p, N) * inforMeasure(i, p, N)
    sum /= N
    return sum
    '''
    Khi N đủ lớn thì approxEntropy sẽ xấp xỉ với Entropy của nguồn tin binomial
    '''

'''
N=10
p=0.5
'''
print('Prob: ', prob(5,0.5, 10))
print('inforMeasure: ', inforMeasure(5,0.5, 10))
print('sumProb: ', sumProb(10,0.5))
print('approxEntropy: ', approxEntropy(10,0.5))
