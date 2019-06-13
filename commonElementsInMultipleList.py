'''
Given three increasingly sorted arrays A, B, C of sizes N1, N2, and N3 respectively, you need to print all common elements in these arrays.

Note: Please avoid printing the same common element more than once.

Input:
First line contains a single integer T denoting the total number of test cases. T testcases follow. Each testcase contains four lines of input. First line consists of 3 integers N1, N2 and N3, denoting the sizes of arrays A, B, C respectively. The second line contains N1 elements of A array. The third lines contains N2 elements of B array. The fourth lines contains N3 elements of C array.

Output:
For each testcase, print the common elements of array. If not possible then print -1.

Constraints:
1 <= T <= 100
1 <= N1, N2, N3 <= 107
1 <= Ai, Bi, Ci <= 1018

Example:
Input:
1
6 5 8
1 5 10 20 40 80
6 7 20 80 100
3 4 15 20 30 70 80 120
Output:
20 80

Explanation:
Testcase1:  20 and 80 are the only common elements
'''


##Solution1 -- Not good .. takes long time

class CommonElements:
    def getCommonElements(this, list1, list2, list3):
        output=""
        for i in list1:
            if i in list2:
                if i in list3:
                    if str(i) not in output:
                        if output:
                            output+= " " + str(i)
                        else:
                            output = str(i)
        if output:
            return output
        else: 
            return -1
        

ce = CommonElements()

num_testcases = int(input())
for i in range(num_testcases):
    count = input()
    list1 = input().split(" ")
    
    
##Solution2 -- 
    
