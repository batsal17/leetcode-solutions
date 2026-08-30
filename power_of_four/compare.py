class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i=0
        while n>=(4**i):
            if n==(4**i):
                return True
            i=i+1
        return False
s1=Solution()
a=int(input("Enter a number: "))
if s1.isPowerOfFour(a):
    print(a,"is power of 4")
else:
    print("Not a power of 4")