class Solution:
    def containsDuplicate(self, nums):
        a=set(nums)
        if len(a)==len(nums):
            return False
        return True
s1=Solution()
b=[1,2,3,4,5,6,7,1]
if s1.containsDuplicate(b):
    print("There is duplicate element")
else:
    print("There is no duplicate element")