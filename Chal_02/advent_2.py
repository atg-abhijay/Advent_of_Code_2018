"""
URL for challenge:
https://adventofcode.com/2018/day/2
"""

def part1():
    f = open("advent_2_input.txt")
    num_twos, num_threes = 0, 0
    for box_id in f.readlines():
        letter_count = {}
        two_found, three_found = False, False
        for letter in box_id:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        for count in letter_count.values():
            if count == 2 and not two_found:
                num_twos += 1
                two_found = True

            if count == 3 and not three_found:
                num_threes += 1
                three_found = True

    print(num_twos*num_threes)


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
