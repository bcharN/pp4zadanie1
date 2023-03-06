

class Stack:
    def __init__(self) -> None:
        self.stack = []
    def push(self, var):
        self.stack.append(var)
    def pop(self):
        lenth = len(self.stack)
        if lenth != 0:
            tmp = self.stack[-1]
            self.stack.pop()
            return tmp
        return None
    def isEmpty(self):
        if len(self.stack) == 0: return True
        else: return False


