"""
URL for challenge:
https://adventofcode.com/2018/day/1
"""

def main():
    f = open("advent_1_input.txt")
    # take the string numbers in the
    # input, map them to integers and
    # convert the map object into a list
    frequencies = list(map(int, f.readlines()))
    return frequencies


def part1():
    frequencies = main()
    print(sum(frequencies))


def part2():
    frequencies = main()
    sums_seen = set()
    sum_so_far = 0
    sums_seen.add(sum_so_far)
    while 1:
        for freq in frequencies:
            sum_so_far += freq
            if sum_so_far in sums_seen:
                print(sum_so_far)
                return

            sums_seen.add(sum_so_far)


def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    if chall == 1:
        part1()
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)

run()
