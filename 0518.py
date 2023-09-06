def solution(players, callings):
    players = dict(zip(players, range(1, len(players)+1)))
    for i in range(len(callings)):
        players[callings[i]] = players[]
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))