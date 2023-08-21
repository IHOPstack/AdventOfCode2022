def main():
    #Gather data
    with open('/Users/devinbeckwith/codezone/Advent/elfCals','r') as f:
        lines = f.read()
        list = lines.split('\n\n')
        masterlist = [string.split('\n') for string in list]
    top3 = [0, 0, 0]
    #add and compare individual calorie count
    for elf in masterlist:
        nums = [int(num) for num in elf]
        calCount = sum(nums)
        if any(calCount > val for val in top3):
            top3.remove(min(top3))
            top3.append(calCount)
    print(sum(top3))
main()

