class Solution:
    def plusOne(self, digits):
        s=0
        for i in range(0,len(digits)):
            s=s*10+digits[i]
        s=s+1
        b=[]
        while s>0:
            b.insert(0,s%10)
            s=s//10
        return b
s1=Solution()
print(s1.plusOne([1,2,3]))

        
