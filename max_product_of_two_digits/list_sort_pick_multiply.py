class Solution:
    def listing(self,n:int)->list:
        list_num=[]
        while n>0:
            list_num.insert(0,n%10)
            n=n//10
        return list_num

    def sorting(self,n1:list)->list:
        l=len(n1)
        for i in range(l):
            swapped=False
            for j in range(0,l-i-1):
                if n1[j]>n1[j+1]:
                    n1[j],n1[j+1]=n1[j+1],n1[j]
                    swapped=True
            if not swapped:
                break
        return n1

    def max_product(self,n1:list)->int:
        return n1[-1]*n1[-2]
    

s1=Solution()
number=int(input("Enter a number in the range [10,10^9]: "))
if number>=10 and number<(10**9):
    print(s1.max_product(s1.sorting(s1.listing(number))))
else:
    print("Number not within the range.")
            
