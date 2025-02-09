f = open("input.txt", "r")
rulesRead = False

#List to save rules
rules = []
#list to save updates
updates = []
#reading the file
for line in f:
    if line == "\n":
        rulesRead = True
        continue
    if not rulesRead:
        line = line.split("|")
        rule = [int(line[0]), int(line[1])]
        rules.append(rule)
    if rulesRead:
        line = line.split(",")
        update = []
        i = 0
        while i < len(line):
           update.append(int(line[i])) 
           i += 1
        updates.append(update)
f.close()
       
invalidUpdates = []
#checking if each update is valid  
for rule in rules:
    for update in updates:
        if rule[0] in update and rule[1] in update:  #if both numbers are in update
            if update.index(rule[0]) > update.index(rule[1]):  #if order isnt correct
                invalidUpdates.append(update)
                updates.remove(update)
                break
              
#finding the middle page number of the valid updates
middlePageNumValid = 0      
for update in updates:
    middlePageNumValid += update[len(update) // 2]
print("Valid updates middle page number:")
print(middlePageNumValid)


#ordering incorrectly oredered updates
continueOrdering = True
while continueOrdering:
    continueOrdering = False
    for update in invalidUpdates:
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    update[update.index(rule[0])] = rule[1]
                    update[update.index(rule[1])] = rule[0]
                    continueOrdering = True
         
middlePageNumInvalid = 0
for update in invalidUpdates:
    middlePageNumInvalid += update[len(update) // 2]
print("Invalid updates middle page number:")
print(middlePageNumInvalid)