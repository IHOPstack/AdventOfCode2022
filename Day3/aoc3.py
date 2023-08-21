def main():
    with open('/Users/devinbeckwith/codezone/Advent/input','r') as f:
        ruckshacks = [line.strip() for line in f]
    itemVals = []
    groups = []
    currentGroup = []
    for ruckshack in ruckshacks:
        index = int(len(ruckshack)/2)
        compartment1 = ruckshack[index:]
        compartment2 = ruckshack[:index]
        for item in compartment1:
            if item in compartment2:
                item = item
                break
        if item.islower():
            itemVal = ord(item)-96
        else:
            itemVal = ord(item)-38
        itemVals.append(itemVal)

        if len(currentGroup) < 3:
            currentGroup.append(ruckshack)
        else:
            groups.append(currentGroup)
            currentGroup = [ruckshack]
    groups.append(currentGroup)
    badgeVals = []
    for currentGroup in groups:
        ruck1 = currentGroup[0]
        ruck2 = currentGroup[1]
        ruck3 = currentGroup[2]
        for item in ruck1:
            if item in ruck2:
                if item in ruck3:
                    badge = item
                    if badge.islower():
                        badgeVal = ord(badge)-96
                    else:
                        badgeVal = ord(badge)-38
                    badgeVals.append(badgeVal)
                    break
    print('itemVals = ', sum(itemVals))
    print('badgeVals = ', sum(badgeVals))
main()