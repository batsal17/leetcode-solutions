class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i=0
        while n>=(3**i):
            if n==3**i:
                return True
            i=i+1
        return False
s1=Solution()
a=int(input("Enter a number: "))
if s1.isPowerOfThree(a):
    print(a,"is power of 3")
else:
    print("Not a power of 3")