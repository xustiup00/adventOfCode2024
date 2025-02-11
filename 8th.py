def createMap(file):
    map = []
    dict = {}
    length = 0
    x, y = 0, 0
    for line in file:
        row = []
        for char in line:
            if char != "\n":
                row.append(char)
                if char != ".":
                    if dict.get(char) == None:
                        dict[char] = []
                    dict[char].append([y, x])
                x += 1
        map.append(row)
        y += 1
        if length == 0:
            length = x
        x = 0
    height = y
    return map, height, length, dict

def setAntinodes(map, dict, height, length):
    count = 0
    antinodes:set = set()
    for letter in dict:
        for first in dict[letter]:
            for second in dict[letter]:
                antinodes.add((first[0], first[1]))
                antinodes.add((second[0], second[1]))
                if first != second:
                    yDif = first[0] - second[0]
                    xDif = first[1] - second[1]
                    y = first[0] + yDif
                    x = first[1] + xDif
                    while True:
                        if 0 <= y < height and 0 <= x < length:
                            antinodes.add((y, x))
                        else:
                            break
                        y += yDif
                        x += xDif
                            
    return len(antinodes)
    
def main():
    f = open("input.txt", "r")
    map, height, length, dict = createMap(f)
    print(setAntinodes(map, dict, height, length))

if __name__ == "__main__":
    main()