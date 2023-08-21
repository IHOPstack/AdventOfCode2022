def main():
    containCount = 0
    overlapCount = 0
    for pair in [line.strip().split(',') for line in open('input', 'r').readlines()]:
        elf1nums = list(map(int, pair[0].split('-')))
        elf2nums = list(map(int, pair[-1].split('-')))
        elf1 = set(range(min(elf1nums), max(elf1nums) + 1))
        elf2 = set(range(min(elf2nums), max(elf2nums) + 1))
        overlap = elf1.intersection(elf2)
        if overlap:
            overlapCount += 1
        if overlap in (elf1, elf2):
            containCount += 1
    print(containCount, overlapCount)
main()