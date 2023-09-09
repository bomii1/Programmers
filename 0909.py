def solution(k, score):
    answer = []
    awardsList = []
    for i in range(len(score)):
        awardsList.append(score[i])
        awardsList.sort(reverse=True)
        if i < k:
            answer.append(awardsList[-1])
        else:
            awardsList.pop()
            answer.append(awardsList[-1])
    return answer
