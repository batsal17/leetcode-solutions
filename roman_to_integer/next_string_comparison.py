class Solution:
    def romanToInt(self, s: str) -> int:
        ls={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        summ=0
        for i in range(0,len(s)):
            first=ls[s[i]]
            if (i+1)<len(s):
                nextt=ls[s[i+1]]
            else:
                nextt=0
            if first>=nextt:
                summ=summ+first
            else:
                summ=summ-first
        return summ

s1=Solution()
roman=input("Enter a roman number: ")
print(s1.romanToInt(roman))
        