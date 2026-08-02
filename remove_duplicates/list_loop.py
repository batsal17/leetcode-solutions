class Solution:
    def removeDuplicates(self, nums):
        a = []

        for i in nums:
            if i not in a:
                a.append(i)

        for i in range(len(a)):
            nums[i] = a[i]

        return len(a)
s1=Solution()
print(s1.removeDuplicates([0,1,1,2,2,2,3,3,3,4]))