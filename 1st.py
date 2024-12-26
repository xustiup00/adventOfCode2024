list1 = [] #left list
list2 = [] #right list

f = open("input.txt", "r")

#divide numbers into lists
for line in f:
  splited = line.split()
  list1.append(int(splited[0]))
  list2.append(int(splited[1]))
          
#sort lists
sortedList1 = sorted(list1)
sortedList2 = sorted(list2)
    
sum = 0  
similarityScore = 0
length = len(sortedList1)
index = 0
#calculate the difference and add up to the sum
while index != length:   
  sum += abs(sortedList1[index] - sortedList2[index])
  similarityScore += (sortedList1[index] * sortedList2.count(sortedList1[index]))
  index += 1

#first answer
print(sum)
#second answer
print(similarityScore)

f.close()