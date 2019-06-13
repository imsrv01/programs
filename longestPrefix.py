'''
Given a array of N strings, find the longest common prefix among all strings present in the array.

Input:
The first line of the input contains an integer T which denotes the number of test cases to follow. Each test case contains an integer N. Next line has space separated N strings.

Output:
Print the longest common prefix as a string in the given array. If no such prefix exists print "-1"(without quotes).

Constraints:
1 <= T <= 103
1 <= N <= 103
1 <= |S| <= 103

Example:
Input:
2
4
geeksforgeeks geeks geek geezer
3
apple ape april

Output:
gee
ap

Explanation:
Testcase 1: Longest common prefix in all the given string is gee.
'''

#### Solution
class longestPrefix:
    def getLongestPrefix(self, stringList, stringCount):
        
        lcp = stringList[0]
        
        for k in range(1,stringCount):
            j=0
            str = stringList[k]
            
            while(j < len(lcp) and j < len(str) and lcp[j:j+1] == str[j:j+1]):
                j+=1
            
            if j == 0:
                return -1
                
            lcp = lcp[0:j]
        
        return lcp
            
longestPrefix = longestPrefix()
num_testcases = int(input())
for i in range(num_testcases):
    stringCount = int(input())
    stringList = input().split(" ")
    print(longestPrefix.getLongestPrefix(stringList,stringCount))
