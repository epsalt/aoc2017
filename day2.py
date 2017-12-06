import csv
from itertools import permutations

## Part 1
def part1(INPUT):
    with open(INPUT) as tsv_in:
        tsv_reader = csv.reader(tsv_in, delimiter='\t')

        checksum = 0
        for line in tsv_reader:
            nums = list(map(int, line))
            checksum = checksum + max(nums) - min(nums)

        return(checksum)

## Part 2
def part2(INPUT):
    with open(INPUT) as tsv_in:
        tsv_reader = csv.reader(tsv_in, delimiter='\t')

        checksum = 0
        for line in tsv_reader:
            perms = permutations(line, 2)
            for perm in perms:
                a, b = map(int, perm)
                if a % b == 0: checksum = checksum + (a / b)

        return(checksum)
