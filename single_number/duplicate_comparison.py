class Solution:
    def singleNumber(self, nums) -> int:
        x=[]
        for i in nums:
            if i in x:
                x.remove(i)
            else:
                x.append(i)
        return x[0]

s1=Solution()
print(s1.singleNumber([4,1,2,1,2]))