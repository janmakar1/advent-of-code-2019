import math


def fuel(num):
    return math.floor(num / 3) - 2


def main():
    input = open("input.txt", "r")
    lines = input.readlines()
    sum = 0
    for line in lines:
        sum += fuel(int(line))
    print(sum)


if __name__ == "__main__":
    main()
