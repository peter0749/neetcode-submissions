class MinStack:

    def __init__(self):
        self.stk = []
        self.mono_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.mono_stk or self.mono_stk[-1] >= val:
            self.mono_stk.append(val)

    def pop(self) -> None:
        if self.mono_stk and self.mono_stk[-1] == self.stk[-1]:
            self.mono_stk.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mono_stk[-1]
