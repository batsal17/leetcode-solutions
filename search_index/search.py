class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        if target<nums[0]:
            return 0
        if target>nums[len(nums)-1]:
            return len(nums)
        for i in range(0,len(nums)):
            if target>nums[i] and target<nums[i+1]:
                return i+1

s1=Solution()
a=[1,3,5,7]
b=5
c=2
print("The index of ",b,'in',a,'is',s1.searchInsert(a,b))
print("The index of ",c,'in',a,'is',s1.searchInsert(a,c))


        