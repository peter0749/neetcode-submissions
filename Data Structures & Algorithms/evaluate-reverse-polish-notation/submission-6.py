class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: int(a/b)
        }
        for token in tokens:
            if token in ops:
                b = stk.pop()
                a = stk.pop()
                c = ops[token](a,b)
                print(f'{c} = {a} {token} {b}')
                stk.append(c)
            else:
                stk.append(int(token))
        return stk[0]