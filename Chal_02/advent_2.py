"""
URL for challenge:
https://adventofcode.com/2018/day/2
"""

def main():
    pass


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