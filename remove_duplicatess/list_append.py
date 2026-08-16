class Solution:
    def containsDuplicate(self, nums):
        a=[]
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                return True
        return False
s1=Solution()
a=[1,2,3,5,6]
if s1.containsDuplicate(a):
    print("There is a duplicate")
else:
    print("There is no duplicate")