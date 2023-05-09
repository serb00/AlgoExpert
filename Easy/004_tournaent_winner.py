def tournamentWinner(competitions, results):
    # Write your code here.
    i = 0
    res = dict()
    while i < len(results):
        home_team, away_ream = competitions[i]
        result = results[i]
        if result == 1:
            if res.get(home_team) is not None:
                res[home_team] = res[home_team] + 3
            else:
                res[home_team] = 3
        else:
            if res.get(away_ream) is not None:
                res[away_ream] = res[away_ream] + 3
            else:
                res[away_ream] = 3

        i += 1

    return max(res, key=res.get)


print(tournamentWinner(
    [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ],
    [0, 0, 1]
))
