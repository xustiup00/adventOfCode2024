import copy

def memmoryArrange(diskMap):
    memAr = []
    length = len(diskMap)
    for k in range(int(diskMap[0])):
        memAr.append(0)
    i = 1
    ID = 1
    while i != length:
        if (i % 2) == 0:
            for k in range(int(diskMap[i])):
               memAr.append(ID)
            ID += 1 
        else:
            for k in range(int(diskMap[i])):
                memAr.append(".")
        i += 1
    return memAr


def moveBlocks(memAr):
    length = len(memAr)
    dotIndex = 0
    numIndex = length - 1
    done = False
    while not done:
        while dotIndex != length and memAr[dotIndex] != ".":
            dotIndex += 1
        if dotIndex == length or dotIndex >= numIndex:
            done = True
            break
        while numIndex != 0 and memAr[numIndex] == ".":
            numIndex -= 1
        if numIndex == 0 or dotIndex >= numIndex:
            done = True
            break
        memAr[dotIndex] = memAr[numIndex]
        memAr[numIndex] = "."
   
        
def moveFiles(memAr):
    #find the last file
    fileEnd = len(memAr) - 1
    while memAr[fileEnd] == ".":
        fileEnd -= 1
        
    fileBeg = fileEnd
    while memAr[fileBeg] == memAr[fileEnd]:
        fileBeg -= 1
    fileBeg += 1
    
    fileLength = fileEnd - fileBeg + 1
    fileCurIndex = memAr[fileBeg]
    #moving files
    while fileCurIndex != "0" and fileBeg > 0:
        freeSpaceBeg = 0
        freeSpaceLength = 0
        while True:
            freeSpaceBeg += freeSpaceLength
            #find free space
            while memAr[freeSpaceBeg] != ".":
                freeSpaceBeg += 1
            freeSpaceEnd = freeSpaceBeg
            while freeSpaceEnd < fileBeg and memAr[freeSpaceEnd] == ".":
                freeSpaceEnd += 1
            freeSpaceEnd -= 1
            freeSpaceLength = freeSpaceEnd - freeSpaceBeg + 1
            if freeSpaceBeg > fileBeg:
                break
            #free space with appropriate length found
            if freeSpaceLength >= fileLength:
                for i in range(fileLength):
                    memAr[freeSpaceBeg + i] = fileCurIndex
                    memAr[fileBeg + i] = "."
                break
        #go to the next file
        fileEnd -= fileLength
        while memAr[fileEnd] == ".":
            fileEnd -= 1
        fileBeg = fileEnd
        while fileBeg >= 0 and memAr[fileBeg] == memAr[fileEnd]:
            fileBeg -= 1  
        fileBeg += 1  
        fileLength = fileEnd - fileBeg + 1
        fileCurIndex = memAr[fileBeg]
               
    
def countSum(memAr):
    index = 0
    length = len(memAr)
    sum = 0
    while index != length:
        if memAr[index] != ".":
            sum += index * int(memAr[index])
        index += 1
    return sum
           

def main():
    f = open("input.txt", "r")
    diskMap = []
    for line in f:
        for i in line:
            diskMap.append(i)
    memAr = memmoryArrange(diskMap)
    memAr2 = copy.deepcopy(memAr)
    moveBlocks(memAr)
    moveFiles(memAr2)
    print("Moving blocks: ", countSum(memAr))
    print("Moving files: ", countSum(memAr2))
    
if __name__ == "__main__":
    main()