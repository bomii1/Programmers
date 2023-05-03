def solution(k, m, score):
    return sum([x*m for i,x in enumerate(sorted(score, reverse=True), start=1) if i % m == 0])

