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
        # fill up the dictionary
        # with different letter counts
        for letter in box_id:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        # if any of the letters have count
        # 2, increment num_twos and set
        # two_found to True so that we don't
        # consider another letter with count 2.
        # similarly for 3
        for count in letter_count.values():
            if count == 2 and not two_found:
                num_twos += 1
                two_found = True

            if count == 3 and not three_found:
                num_threes += 1
                three_found = True

    print(num_twos*num_threes)


def part2():
    f = open("advent_2_input.txt")
    box_ids = [line.strip() for line in f.readlines()]
    stop = False
    # compare each box id with the
    # box ids that follow it. compare
    # them letter by letter and keep
    # track of number of differences
    # and the index at which they are
    # different
    for idx, b_id in enumerate(box_ids[:-1]):
        for other_b_id in box_ids[idx+1:]:
            num_different = 0
            idx_different = -1
            for i, letter in enumerate(b_id):
                if b_id[i] != other_b_id[i]:
                    num_different += 1
                    idx_different = i

            # if the ids are only different
            # in one place, print either of
            # the box ids except the differing
            # character. we can stop now and break
            # out of all the loops
            if num_different == 1:
                print(b_id[:idx_different] + b_id[idx_different+1:])
                stop = True
                break

        if stop:
            break


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
