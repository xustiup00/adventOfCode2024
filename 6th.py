import copy

#returns number of possible loops
def loopCheck(map, guardPosition, height, width, todo):
    xObs, yObs, countLoops = 0, 0, 0
    while xObs < width:
        while yObs < height:
            if [xObs, yObs] != guardPosition and map[yObs][xObs] != "#" and todo[yObs][xObs]:
                coordinates:set = set()
                cpyMap = copy.deepcopy(map)
                cpyMap[yObs][xObs] = "#"
                x, y = guardPosition
                direction = 0
                while y >= 0 and y < height and x >= 0 and x < width:
                    if (x, y, direction) in coordinates:
                        countLoops += 1
                        break

                    coordinates.add((x, y, direction))
                    
                    if direction == 0:
                        if y - 1 >= 0 and cpyMap[y - 1][x] == "#":
                            direction = 1
                        else:
                            y -= 1
                    elif direction == 1:
                        if x + 1 < width and cpyMap[y][x + 1] == "#":
                            direction = 2
                        else:
                            x += 1
                    elif direction == 2:
                        if y + 1 < height and cpyMap[y + 1][x] == "#":
                            direction = 3
                        else:
                            y += 1
                    elif direction == 3:
                        if x - 1 >= 0 and cpyMap[y][x - 1] == "#":
                            direction = 0
                        else:
                            x -= 1
                                   
            yObs += 1
        xObs += 1   
        yObs = 0     
    return countLoops
    
def parse():
    f = open("input.txt", "r")

    #finding height and length
    height = 0
    width = 0
    map = []
    for line in f:
        row = []
        for i in line:
            if i != "\n":
                row.append(i)
        if width == 0:
            width = len(row)  
        map.append(row)  
        height += 1 
    f.close()

    #finding guard position 
    x = 0
    y = 0
    for j in range(height):
        for i in range(width):
            if map[j][i] == "^":
                x = i
                y = j
                
    return height,width,map,x,y

height, width, map, x, y = parse()
 
        
#predicting the guard's route and counting visited positions
todo = [[False for _ in range(width)] for _ in range(height)]

direction = 0 #0 - up, 1 - right, 2 - down, 3 - left
count = 0
while y >= 0 and y < height and x >= 0 and x < width:
    if map[y][x] != "X":
        map[y][x] = "X"
        count += 1
    todo[y][x] = True
    
    if direction == 0:
        if map[y - 1][x] == "#":
            direction = 1
        else:
            y -= 1
    elif direction == 1:
        if map[y][x + 1] == "#":
            direction = 2
        else:
            x += 1
    elif direction == 2:
        if y != height - 1 and map[y + 1][x] == "#":
            direction = 3
        else:
            y += 1
    elif direction == 3:
        if map[y][x - 1] == "#":
            direction = 0
        else:
            x -= 1
            
height, width, map, x, y = parse()         

loopPositions = loopCheck(map, [x, y], height, width, todo)           
            
print("visited positions:", count)
print("possible loop could been created:", loopPositions)

