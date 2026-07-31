class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if (i==')' and top!='(') or (i==']' and top!='[') or (i=='}' and top!='{'):
                    return False
        return len(stack)==0
s1=Solution()
s=input("Enter parenthesis for checking: ")
if (s1.isValid(s)==True):
    print("Valid")
else:
    print("Invalid")
