class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:len(needle)+i]==needle:
                return(i)
        return -1
s1=Solution()
a=input("Enter haystack: ")
b=input("Enter needle: ")
print(s1.strStr(a,b))