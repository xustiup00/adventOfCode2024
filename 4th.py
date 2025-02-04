f = open("/home/polina/Desktop/adventOfCode2024/input.txt", "r")
count = 0
pattern = "XMAS"
dirChange = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
array = []
w, h = 0, 0
    
#copy the input into 2d array and determine height and width
for line in f:
    row = []
    for i in line:
        row.append(i)
    h += 1
    array.append(row)
    if w == 0:
        w = len(row)
        
#count patterns of XMAS
for i in range(h):
    for j in range(w - 1):
        if array[i][j] == pattern[0]:
            for direction in dirChange:
                x = i
                y = j
                found = True
                for k in range(1, len(pattern)):
                    x += direction[0]
                    y += direction[1]
                    if x < 0 or x >= h or y < 0 or y >= w - 1 or array[x][y] != pattern[k]:
                        found = False
                        break
                if found:
                    count += 1 
print("Number of XMAS:")
print(count)
   
#count patterns of MASMAS
count = 0    
for i in range(h):
    for j in range(w - 1):
        if array[i][j] == "A" and i > 0 and i < h - 1 and j > 0 and j < w - 2:
            if (array[i - 1][j - 1] == "M" and array[i - 1][j + 1] == "S" and array[i + 1][j + 1] == "S" and array[i + 1][j - 1] == "M") or \
                (array[i - 1][j - 1] == "M" and array[i - 1][j + 1] == "M" and array[i + 1][j + 1] == "S" and array[i + 1][j - 1] == "S") or \
                (array[i - 1][j - 1] == "S" and array[i - 1][j + 1] == "M" and array[i + 1][j + 1] == "M" and array[i + 1][j - 1] == "S") or \
                (array[i - 1][j - 1] == "S" and array[i - 1][j + 1] == "S" and array[i + 1][j + 1] == "M" and array[i + 1][j - 1] == "M"):
                    count += 1

print("number of MAS:")
print(count)
f.close()