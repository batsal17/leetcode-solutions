class Solution:
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left

s1=Solution()
a=[1,3,5,7]
b=5
c=2
print("The index of ",b,'in',a,'is',s1.searchInsert(a,b))
print("The index of ",c,'in',a,'is',s1.searchInsert(a,c))