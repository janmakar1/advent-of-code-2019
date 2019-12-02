import math


def fuel(num):
    return math.floor(num / 3) - 2


def fuel2(num):
    sum = 0
    while fuel(num) >= 0:
        sum += fuel(num)
        num = fuel(num)
    return sum


def main():
    input = open("input.txt", "r")
    lines = input.readlines()
    total_sum = 0
    for line in lines:
        total_sum += fuel2(int(line))
    print(total_sum)


if __name__ == "__main__":
    main()
