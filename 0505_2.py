def solution(t, p):
    count = 0
    for i in range(0,len(t)):
        if i+len(p) > len(t):
            break
        if t[i:i+len(p)] <= p:
            print(t[i:i+len(p)], ",", p)
            count += 1
    return count