class Solution:
    def addDigits(self, num):
        s=0
        while num//10!=0:
            while num!=0:
                r=num%10
                s=s+r
                num=num//10
            if s//10==0:
                return s
            num=s
            s=0
        return num
s1=Solution()
print(s1.addDigits(89))

