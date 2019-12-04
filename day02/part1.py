# maybe some refactoring but later..

# processCommand returns result: string
def processCommand(opcode, idx_of_operand1, idx_of_operand2, data):
    result = int()
    operand1 = int(data[idx_of_operand1])
    operand2 = int(data[idx_of_operand2])
    if(opcode == 1):
        result = operand1 + operand2
    elif (opcode == 2):
        result = operand1 * operand2
    elif opcode == 99:
        print("OPCODE 99 WILL HALT PROGRAM..")
    else:
        print("WRONG OPCODE NEED FURTHER INSTRUCTIONS..")
    return result


def mainLoop(data):
    for i in range(0, len(data), 4):
        # print(i, data[i])
        if(int(data[i]) == 99):
            break
        else:
            result = processCommand(int(data[i]), int(data[i+1]), 
            int(data[i+2]), data)
            # print(f"will save result {result} into index {data[i+3]}")
            data[data[i+3]] = result

    print(data)
    print(f">> Answer is: {data[0]}") # answer: 2692315 

    dataStr = [str(d) for d in data]
    output = ",".join(dataStr)
    print(output)


def parseFile(filename):
    input = open(filename, "r")
    program_code = input.readline()
    program_code = program_code.rstrip()
    dataStr = program_code.split(",")
    data = [int(d) for d in dataStr]
    input.close() # do i need to do this?
    return data



data = parseFile("input.txt")

# 1202 procedure
data[1] = 12
data[2] = 2

# MAIN LOOP
mainLoop(data)