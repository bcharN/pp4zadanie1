

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


if __name__=="__main__":
    st1 = Stack()
    
    for i in range(1,10):
        st1.push(i)
    while(not st1.isEmpty()):
        print(st1.pop())
    print(st1.pop())

