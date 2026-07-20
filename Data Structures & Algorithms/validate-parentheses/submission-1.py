class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c ==')' and stk and stk[-1] == '(':
                stk.pop()
            elif c =='}' and stk and stk[-1] == '{':
                stk.pop()
            elif c ==']' and stk and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(c)
        return not stk