
def incDecCheck(list):
    index = 0
    inc = 0
    dec = 0
    increasing = True
    length = len(list)
    while index + 1 != length:
        if int(list[index]) < int(list[index + 1]):
            inc += 1
        elif int(list[index]) > int(list[index + 1]):
            dec += 1
        index += 1
    if inc > dec:
        increasing = True
    else:
        increasing = False
    return increasing

def check(list, increasing):
    length = len(list)
    index = 0
    safe = True
    while index + 1 != length:
            distance = abs(int(list[index]) - int(list[index + 1]))
            if not 1 <= distance <= 3 or (increasing and (int(list[index]) > int(list[index + 1]))) \
            or (not increasing and (int(list[index]) < int(list[index + 1]))):
                safe = False
                break
            index += 1
    return safe


f = open("/home/polina/Desktop/adventOfCode2024/input.txt", "r")
safeLines = 0
for line in f:
    splitted = line.split()
    length = len(splitted)
    safe = False  #actual line is not safe
    increasing = incDecCheck(splitted)
    safe = check(splitted, increasing)
    removeIndex = 0
    while not safe and removeIndex != length:
        splittedWithRemove = splitted.copy()
        splittedWithRemove.pop(removeIndex)
        increasing = incDecCheck(splittedWithRemove)
        safe = check(splittedWithRemove, increasing)
        removeIndex += 1
    if safe:
        safeLines += 1 
print(safeLines)