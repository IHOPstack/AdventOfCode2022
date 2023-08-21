def main():
    with open('/Users/devinbeckwith/codezone/Advent/2strat','r') as f:
        lines = [line.strip().split() for line in f.readlines()]
    score = 0
    win = 6
    draw = 3
    matchup = {'X':['C','A','B'],'Y':['A','B','C'],'Z':['B','C','A']}
    shapeScore = {'A':1, 'B':2, 'C':3}
    for line in lines:
        opponent = line[0]
        outcome = line[1]
        playerInd = shapeScore[opponent] - 1
        player = matchup[outcome][playerInd]
        if outcome == 'Y':
            score += draw
        elif outcome == 'Z':
            score += win
        score += shapeScore[player]
    print(score)
main()
