evenList = []

listNumber = int(input("Enter the Total List Items = "))
for i in range(1, listNumber + 1):
    listValue = int(input("Enter the %d List Item = " %i))
    evenList.append(listValue)

print("List Items = ", evenList)
i = 0

while (i < len(evenList)):
    if (evenList[i] % 2 == 0):
        evenList.remove(evenList[i])
    i = i + 1
    
print("List Items after removing even Items = ", evenList)
