class Solution:
    def max_product(self,n:int)->int:
        largest=0
        second_largest=0
        while n>0:
            a=n%10
            n=n//10
            if a>largest:
                second_largest=largest
                largest=a
            elif a>second_largest:
                second_largest=a
        return largest*second_largest

s1=Solution()
number=int(input("Enter a number in the range [10,10^9]: "))
if number>=10 and number<(10**9):
    print(s1.max_product(number))
else:
    print("Number not within the range.")

