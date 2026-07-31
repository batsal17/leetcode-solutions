class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        a={')':'(',
        ']':'[',
        '}':'{'}
        for i in s:
            if i in a.values():
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if top!=a[i]:
                    return False
        return len(stack)==0
s1=Solution()
s=input("Enter parenthesis for checking: ")
if (s1.isValid(s)==True):
    print("Valid")
else:
    print("Invalid")