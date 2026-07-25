class Solution:
    def max_product(self,n:int)->int:
        n_list=[int(d) for d in str(n)]
        n_list.sort()
        return n_list[-1]*n_list[-2]

s1=Solution()
number=int(input("Enter a number in the range [10,10^9]: "))
if number>=10 and number<(10**9):
    print(s1.max_product(number))
else:
    print("Number not within the range.")
