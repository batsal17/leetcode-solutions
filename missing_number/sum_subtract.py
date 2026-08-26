class Solution:
    def missingNumber(self, nums):
        l=len(nums)
        sum1=(l*(l+1))//2
        summ=0
        for i in nums:
            summ=summ+i
        return sum1-summ
s1=Solution()
print(s1.missingNumber([0,1,2,4]))