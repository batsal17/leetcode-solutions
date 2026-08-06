class Solution:
    def lengthOfLastWord(self, s):
        st=s.rstrip()
        l=len(st)
        m=l
        while m>0 and st[m-1]!=' ':
            m=m-1
        return l-m
s1=Solution()
a=input("Enter a sentence: \n")
print(s1.lengthOfLastWord(a))