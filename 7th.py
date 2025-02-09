#operations: 0 = +, 1 = *, 2 = ||
def makeOperation(numbers, index, operation, result, testValue):
    if index != len(numbers):
        res = 0
        if operation == 0:
            res = result + int(numbers[index])
        elif operation == 1:
            res = result * int(numbers[index])
        else:
            res = str(result) + numbers[index]
            res = int(res)
        if index + 1 == len(numbers):
            return res == testValue
        return makeOperation(numbers, index + 1, 0, res, testValue) or makeOperation(numbers, index + 1, 1, res, testValue) \
            or makeOperation(numbers, index + 1, 2, res, testValue)



def main():
    f = open("input.txt", "r")
    calibResult = 0
    for line in f:
        splited = line.split(":")
        testValue = int(splited[0])
        numbers = splited[1].split()
        res1 = int(numbers[0]) + int(numbers[1])
        res2 = int(numbers[0]) * int(numbers[1])
        res3 = numbers[0] + numbers[1]
        if makeOperation(numbers, 2, 0, res1, testValue) or makeOperation(numbers, 2, 1, res1, testValue) \
            or makeOperation(numbers, 2, 2, res1, testValue) or makeOperation(numbers, 2, 0, res2, testValue) \
            or makeOperation(numbers, 2, 1, res2, testValue) or makeOperation(numbers, 2, 2, res2, testValue) \
            or makeOperation(numbers, 2, 0, int(res3), testValue) or makeOperation(numbers, 2, 1, int(res3), testValue) \
            or makeOperation(numbers, 2, 2, int(res3), testValue):
            calibResult += int(testValue)
    print (calibResult)
     
if __name__=="__main__":
    main()   