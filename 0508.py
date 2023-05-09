def solution(s):
    s = sorted([int(x) for x in s.split()])
    return str(s[0]) + " " + str(s[-1])