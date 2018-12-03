"""
URL for challenge:
https://adventofcode.com/2018/day/1
"""

def main():
    f = open("advent_1_input.txt")
    frequencies = list(map(int, f.readlines()))
    return frequencies

def part1():
    frequencies = main()
    print(sum(frequencies))


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
