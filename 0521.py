def solution(s):
    s = s.split(" ")
    answer = []
    trans = lambda i, x: x.upper() if i % 2 == 1 else x.lower()
    for i in range(len(s)):
        word = []
        for j in range(len(s[i])):
            word.append(trans(j+1, s[i][j]))
        answer.append(("".join(word)))
    return " ".join(answer)