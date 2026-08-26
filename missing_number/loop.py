class Solution:
    def missingNumber(self, nums):
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
s1=Solution()
print(s1.missingNumber([0,1,2,4]))