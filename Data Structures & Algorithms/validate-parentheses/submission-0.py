class Solution:
    def isValid(self, s: str) -> bool:
        Map = { ')': '(',
                ']': '[',
                '}': '{'}
        stack = []
        for c in s:
            if c not in Map:
                stack.append(c)
            else: # c is closing bracket
                if not stack or stack[-1] != Map[c]:
                    return False
                stack.pop()
        return len(stack) == 0
        

# if is open bracket:
#   push to stack
# else if is closing:
#   check stack top is matching
#   if  match
#       POP AND check the next one
#   else 
#       

        