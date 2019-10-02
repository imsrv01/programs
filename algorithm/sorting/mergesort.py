def mergesort(list):
    low = 0
    high = len(list)-1
    #print('array length - ', len(list), low, high)
    if len(list) == 1:
        return list
    mid = (low + high )/2

    listL = list[low:mid+1]
    listR = list[mid+1:high+1]

    print(listL)
    print(listR)
    #print('mid - ', mid)
    listL = mergesort(listL)
    listR = mergesort(listR)

    return merge(listL, listR)


def merge(list1, list2):
    print('merge --- ', list1, list2)
    i=0
    j=0
    k=0
    list3=[]

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i = i + 1
        else:
            list3.append(list2[j])
            j = j + 1

    for i in range(i, len(list1)):
        list3.append(list1[i])

    for j in range(j, len(list2)):
        list3.append(list2[j])

    return list3

list1=[2,4,8,32,97,765,890]
list2=[6,9,78,81,108]
list = [32,9,57,45,10, 12 , 39, 11]
#merge(list1,list2)

print('SORTED list - ', mergesort(list))
