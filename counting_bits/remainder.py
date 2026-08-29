class Solution:
    def countBits(self, n):
        b=[]
        for j in range(0,n+1):
            i=j
            count=0
            while i!=0:
                count=count+i%2
                i=i//2
            b.append(count)
        return b
s1=Solution()
print(s1.countBits(7))