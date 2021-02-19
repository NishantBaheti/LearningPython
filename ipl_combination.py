
from itertools import combinations

def pairings(list_of_teams):
    pairs = []
    combs = combinations(list_of_teams,2)
    total_pairs = 0
    for comb in combs:
        pairs.append(str(comb[0]) + "-VS-" + str(comb[1]))
        total_pairs += 1
    return pairs,total_pairs

if __name__ == "__main__":
    list_of_teams = []
    while True:
        v = input()
        if v == "Q":
            break
        else:
            list_of_teams.append(v)
    pairs,total_pairs = pairings(list_of_teams)
    print(total_pairs)
    for i in pairs:
        print(i)
