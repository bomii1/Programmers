import math

def solution(n):
    cnt = 0
    for i in range(2, n+1):
        if isPrime(i):
            cnt += 1
    return cnt
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

"""
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,int(math.sqrt(n))+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
print(solution(10))
"""