from collections import Counter

def solution(X, Y):
    answer = Counter(X) & Counter(Y)
    return "-1" if len(answer) == 0 else "".join(sorted(answer, reverse=True)) if len(answer) == 1 else "".join(sorted(list(answer.elements()), reverse=True))


X = "5525"
Y = "1255"

print(solution(X, Y))