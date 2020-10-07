import math

def prob(n, p):
    '''
        p là xác suất có được mặt ngửa
        n là số lần tung để có được mặt ngửa
    '''
    return ((1-p)**(n-1))*p

def inforMeasure(n, p):
    return -math.log2( prob(n, p) )

def sumProb(N, p):
    ans = 0
    for i in range(1,N+1):
        ans += prob(i, p)
    return ans
    '''
        Ta có tổng xác suất các symbols:
            ans = (1-p)^0 * p + (1-p)^1 * p + (1-p)^2 * p + ... + (1-p)^n-1 * p
            ans = p(1/p) = 1. (cấp số nhân lùi vô hạn vì |p| < 1)
    '''

def approxEntropy(N, p):
    sum = 0
    for i in range(1,N+1):
        sum =+ prob(i, p) * inforMeasure(i, p)
    sum /= N
    return sum
    '''
    Khi N đủ lớn thì approxEntropy sẽ xấp xỉ với Entropy của nguồn tin geometric
    '''

print('Prob: ', prob(5,0.5))
print('inforMeasure: ', inforMeasure(5,0.5))
print('sumProb: ', sumProb(70,0.5))
print('approxEntropy: ', approxEntropy(10,0.5))
