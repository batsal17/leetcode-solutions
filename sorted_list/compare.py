class Solution:
    def merge(self, nums1, m, nums2, n):
        while len(nums1)<(m+n):
            nums1.append(0)
        a=0
        b=0
        while b<n:
            if a<m+b and nums1[a]<=nums2[b]:
                a=a+1
            else:
                nums1.insert(a,nums2[b])
                nums1.pop()
                b=b+1
        return nums1
s1=Solution()
print(s1.merge([1,2,3],3,[2,5,6],3))
                

                
        