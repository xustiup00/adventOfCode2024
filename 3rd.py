f = open("input.txt", "r")
content = f.read()
sum = 0
index = 0
length = len(content)
disabled = False


while index != length:
    if content[index] == "d" and content[index + 1] == "o":
        if content[index + 2] == "(" and content[index + 3] == ")":
            disabled = False
            index += 4
        elif content[index + 2] == "n" and content[index + 3] == "'" and content[index + 4] == "t" and content[index + 5] == "(" and content[index + 6] == ")":
            disabled = True
            index += 7
    if content[index] == "m" and content[index + 1] == "u" and content[index + 2] == "l" and content[index + 3] == "(":
        firstArg = ""
        secondArg = ""
        index += 4
        while content[index].isdigit():
            firstArg += content[index]
            index += 1
        if content[index] != "," or firstArg == "":
            continue
        index += 1
        while content[index].isdigit():
            secondArg += content[index]
            index+= 1
        if content[index] != ")" or secondArg == "":
            continue
        if not disabled:
            sum += int(firstArg) * int(secondArg)
    index += 1

print(sum)
f.close()
    