class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ')}]':
                if not stk:
                    return False
                if c == ')' and stk[-1] != '(':
                    return False
                if c == '}' and stk[-1] != '{':
                    return False
                if c == ']' and stk[-1] != '[':
                    return False
                stk.pop()
            else:
                stk.append(c)
        return not stk