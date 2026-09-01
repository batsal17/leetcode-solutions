class Solution:
    def hammingWeight(self, n):
        a=0
        while n>=1:
            r=n%2
            a=a+r
            n=n//2
        return a
s1=Solution()
print(s1.hammingWeight(11))

