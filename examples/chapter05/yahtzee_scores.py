#!/usr/bin/env python3
def printScore(player, **scores):
    totalScore = 0
    print("Player:", player)
    for category, score in scores.items():
        print("{0:>15}: {1}".format(category, score))
        totalScore += score
    print("{0:>15}: {1}".format("Total", totalScore))


printScore("Aiden", Aces=4, Twos=8, FullHouse=25,
           LgStraight=40)
printScore("Cindy", Twos=4, LgStraight=40, Chance=24,
           ThreeOfAKind=21)
