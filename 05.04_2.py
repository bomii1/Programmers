def solution(n):
    return min([x for x in range(2,n) if n % x == 1])