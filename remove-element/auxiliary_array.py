class Solution:
    def removeElement(self, nums,val):
        b=[]
        for i in nums:
            if i!=val:
                b.append(i)
        for i in range(len(b)):
            nums[i]=b[i]
        print(nums)
        print(b)
        return len(b)
s1=Solution()
a=[1,2,3,4,5,5,2]
print(s1.removeElement(a,5))
    
