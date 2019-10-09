

def buildTable(str):
    list1 = list(str)
    j = 0
    list2=[]
    for i in range(len(list1)):
        if i == 0:
            list2.append(0)
        else:
            if list1[j] == list1[i]:
                list2.append(j+1)
                j = j+1
            else:
                list2.append(0)
    return list2


def kmpSearch(str, searchStr):

    refTable = buildTable(searchStr)
    list1 = list(str)
    list2 = list(searchStr)
    j=0
    n = len(list1)
    for i in range(n):
        if list1[i] == list2[j]:
            j = j + 1
        else:
            if j > 0 and refTable[j-1] > 0:
                j = refTable[j-1]
            else:
                j=0
            if list1[i] == list2[j]:
                j = j+1
        if j >= len(list2):
            return  (i-(len(list2)-1))
    return -1

print(buildTable('gstbngscp'))
print(kmpSearch('ABCDABCDABDE','ABCDABD' ))
