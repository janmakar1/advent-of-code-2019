MIN = 152085
MAX = 670283


def areTwoAdjacentDigitsTheSame(num):
    try:
        for idx in range(len(str(num))):
            curr, nextt = str(num)[idx], str(num)[idx+1]
            # print(curr, nextt)
            if(curr == nextt):
                return True
    except IndexError:
        pass
    return False


def isNotDecreasing(num):
    guard = str(num)[0]
    for elem in str(num):
        if(int(elem) > int(guard)):
            guard = elem
        if(int(elem) < int(guard)):
            return False
    return True


# conditions that password must 6 chars and between min max are always true
# so i am not checking it (in my implementation)
def isPasswordValid(num):
    return areTwoAdjacentDigitsTheSame(num) and isNotDecreasing(num)


# output to file was implemented due to debugging purposes
def main(output=None):
    if(output):
        fileOutput = open(output, "w")
    amountOfValidPasswords = 0
    for i in range(MIN, MAX):
        if(isPasswordValid(i)):
            if(output):
                fileOutput.write(str(i)+'\n')
            amountOfValidPasswords += 1
    if(output):
        fileOutput.write(f"TOTAL: {amountOfValidPasswords}")
        fileOutput.close()
    print(f"TOTAL: {amountOfValidPasswords}")
    return amountOfValidPasswords


main()
